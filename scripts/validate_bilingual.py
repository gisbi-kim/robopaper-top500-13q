"""Validate complete translations, reading structure, and navigation in both editions."""
from collections import Counter
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup

from build_bilingual import ROOT, KOREAN, strip_generated, targets


def numbers(text):
    # Korean “제3자” translates to “third party”, rather than a numerical result.
    return Counter(re.findall(r'\d+(?:[.,]\d+)*', text.replace('제3자', 'third party')))


def validate():
    translations = json.loads((ROOT / 'translations/en.json').read_text(encoding='utf-8'))
    pages = {path: BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
             for path in list(ROOT.glob('*.html')) + list((ROOT / 'en').glob('*.html'))}
    assert len(pages) == 24, f'Expected 24 pages, found {len(pages)}'
    for path, soup in pages.items():
        english = path.parent.name == 'en'
        language = 'en' if english else 'ko'
        assert soup.html['lang'] == language, path
        assert len(soup.select('.language-bar')) == 1, path
        assert len(soup.select('.translation-note')) == 1, path
        assert len(soup.select('[data-language]')) == 2, path
        assert soup.select_one('[aria-current="page"]')['data-language'] == language, path
        assert len(soup.select('link[rel="alternate"][hreflang]')) == 2, path
        assert soup.select_one('link[rel="canonical"]'), path
        assert not soup.select('script[src]'), f'Page must remain self-contained: {path}'
        expected = 0 if path.name == 'index.html' else 500 if 'apple_style' in path.name else 50
        cards = soup.select('article.paper-card')
        assert len(cards) == expected, (path, len(cards))
        for card in cards:
            assert len(card.select('.summary-row')) == 13, (path, card['id'])
            assert all(row.get_text(strip=True) for row in card.select('.row-text')), (path, card['id'])
        for link in soup.select('a[href]'):
            url = urlsplit(link['href'])
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            assert target in pages, (path, link['href'])
            if url.fragment:
                assert pages[target].find(id=unquote(url.fragment)), (path, link['href'])
        if english:
            for node in soup.find_all(string=KOREAN):
                assert node.parent.get('data-language') == 'ko', (path, str(node))
            original = pages[ROOT / path.name]
            ko_cards = original.select('article.paper-card')
            assert [c['id'] for c in cards] == [c['id'] for c in ko_cards], path
            assert [a['href'] for a in soup.select('a:not([data-language])')] == [a['href'] for a in original.select('a:not([data-language])')], f'Source links changed: {path}'
            for ko, en in zip(ko_cards, cards):
                assert ko.h2.get_text() == en.h2.get_text(), (path, ko['id'])
                for a, b in zip(ko.select('.one-line, .row-text'), en.select('.one-line, .row-text')):
                    assert numbers(a.get_text()) == numbers(b.get_text()), (path, ko['id'], a.get_text(), b.get_text())
                assert len(ko.select('strong')) == len(en.select('strong')), (path, ko['id'], 'emphasis changed')
        else:
            clean = BeautifulSoup(strip_generated(path.read_text(encoding='utf-8')), 'html.parser')
            for element in targets(clean):
                key = element.decode_contents()
                assert key in translations and translations[key].strip(), (path, key)
    print('PASS: 24 pages; 500 papers and 6,500 rows per complete edition; '
          '10 matching chunks; complete English coverage; numbers, titles, source links, '
          'anchors, language controls, and standalone assets verified.')


if __name__ == '__main__':
    validate()
