"""Build static English pages and inline the language controls; no network calls."""
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
KOREAN = re.compile('[가-힣]')
BASE_URL = 'https://gisbi-kim.github.io/robopaper-top500-13q/'


def targets(soup):
    found = {}
    for node in soup.find_all(string=KOREAN):
        if node.parent.name in ('style', 'script'):
            continue
        tag = node.parent
        block = tag.find_parent(class_=lambda c: c in ('row-text', 'one-line', 'subtitle'))
        if block:
            tag = block
        found[id(tag)] = tag
    return list(found.values())


def strip_generated(source):
    return re.sub(r'<!-- bilingual:[a-z]+ -->.*?<!-- /bilingual:[a-z]+ -->', '', source, flags=re.S)


def decorate(source, filename, language):
    english = language == 'en'
    ko_path = '../' + filename if english else filename
    en_path = filename if english else 'en/' + filename
    canonical = BASE_URL + ('en/' if english else '') + filename
    css = (ROOT / 'scripts/language.css').read_text(encoding='utf-8')
    js = (ROOT / 'scripts/language.js').read_text(encoding='utf-8')
    head = f'''<!-- bilingual:head -->
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="ko" href="{BASE_URL + filename}">
  <link rel="alternate" hreflang="en" href="{BASE_URL + 'en/' + filename}">
  <script>{js}</script>
  <style>{css}</style>
<!-- /bilingual:head -->'''
    source = source.replace('</head>', head + '</head>')
    current_ko = '' if english else ' aria-current="page"'
    current_en = ' aria-current="page"' if english else ''
    nav = f'''<!-- bilingual:nav -->
    <nav class="language-bar" aria-label="{'Language selection' if english else '언어 선택'}">
      <span class="language-caption">{'Reading language' if english else '읽기 언어'}</span>
      <div class="language-options">
        <a class="language-option" data-language="ko" lang="ko" hreflang="ko" href="{ko_path}?lang=ko"{current_ko}>한국어</a>
        <a class="language-option" data-language="en" lang="en" hreflang="en" href="{en_path}?lang=en"{current_en}>English</a>
      </div>
    </nav>
<!-- /bilingual:nav -->'''
    source = re.sub(r'(<main class="page">)', lambda m: m[1] + nav, source, count=1)
    note = ('English summaries are machine translations of the Korean reading notes. '
            'Check technical details, numerical results, and resource availability against the original papers.'
            if english else
            '영어 요약은 한국어 연구 노트의 기계 번역입니다. 기술적 세부 사항, 수치와 공개 자원 여부는 원문 논문에서 확인해 주세요.')
    # Put the notice in the hero, after its actions and before the next section.
    source = re.sub(r'(</section>)', lambda m: f'<!-- bilingual:note -->\n<p class="translation-note">{note}</p>\n<!-- /bilingual:note -->' + m[1], source, count=1)
    return source


def build():
    translations = json.loads((ROOT / 'translations/en.json').read_text(encoding='utf-8'))
    (ROOT / 'en').mkdir(exist_ok=True)
    for path in sorted(ROOT.glob('*.html')):
        original = strip_generated(path.read_text(encoding='utf-8'))
        soup = BeautifulSoup(original, 'html.parser')
        for element in targets(soup):
            key = element.decode_contents()
            translated = translations[key]
            element.clear()
            for child in list(BeautifulSoup(translated, 'html.parser').contents):
                element.append(child)
        soup.html['lang'] = 'en'
        soup.title.string = soup.title.get_text() + ' · English'
        (ROOT / 'en' / path.name).write_text(decorate(str(soup), path.name, 'en'), encoding='utf-8')
        path.write_text(decorate(original, path.name, 'ko'), encoding='utf-8')
        print(f'Built ko/en: {path.name}')


if __name__ == '__main__':
    build()
