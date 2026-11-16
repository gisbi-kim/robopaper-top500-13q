# RoboPaper Top-500 13Q

Structured summaries of the top-cited robotics papers from RoboPaper Atlas, organized with a 13-question insight framework.

Live site: https://gisbi-kim.github.io/robopaper-top500-13q/

## What This Is

This repository publishes a self-contained HTML reading bundle for 500 highly cited robotics papers from the RoboPaper Atlas paper explorer.

Each paper card is available in Korean and English using 13 fixed research-reading questions. Use the **한국어 / English** controls at the top of every page. The English edition covers all 500 papers and all 6,500 summary rows, including the ten smaller reading pages.

The original Korean edition is at the [site root](https://gisbi-kim.github.io/robopaper-top500-13q/); the [English edition](https://gisbi-kim.github.io/robopaper-top500-13q/en/) is under `en/`. Internal navigation stays in the selected edition. Language switching preserves the page, query parameters, and paper anchor; the choice is remembered when browser storage is available. An explicit `?lang=ko` or `?lang=en` takes precedence. The language links also work without JavaScript or storage.

The 13 questions are:

1. Background
2. Problem
3. Prior limitations
4. Goal
5. Method
6. Core idea
7. Validation
8. Results
9. Comparison
10. Significance
11. Limitations
12. Future work
13. Public resources

The goal is not to replace the papers, but to make their research context, technical contribution, validation setup, limitations, and released resources easier to scan.

## Sources

- Paper ranking and metadata source: [RoboPaper Atlas](https://gisbi-kim.github.io/robopaper-atlas/index.html)
- Reading structure reference: [13 Questions for Deep Paper Reading](https://gisbi-kim.github.io/paper-reading-13-questions/)

The summaries use paper metadata and citation information from the RoboPaper Atlas snapshot, which combines DBLP, Crossref, OpenAlex, DOI deduplication, and Semantic Scholar citation counts as described on the original Atlas page.

## Files

- `index.html`: Home page and navigation entry.
- `paper_summaries_apple_style.html`: Full 500-paper integrated HTML page.
- `paper_summaries_chunk_001_050.html` through `paper_summaries_chunk_451_500.html`: 50-paper subpages for faster browsing.
- `en/`: Complete static English counterparts of all 12 HTML pages.
- `translations/en.json`: Korean HTML fragments mapped to their English translations; shared by the full collection and chunk pages.
- `scripts/build_bilingual.py`: Offline generator for English pages and the language controls.
- `scripts/language.js` and `scripts/language.css`: Language preference behavior and accessible, responsive controls, inlined into every generated page to preserve standalone use.
- `scripts/validate_bilingual.py`: Checks translation coverage, paper/row counts, numeric content, source links, local navigation, and matching editions.

The older local Google-style export is intentionally not part of the published bundle.

## Design

The pages use a bright, restrained Apple-style layout with large paper cards, single-column summary rows, subtle shadows, rounded corners, and responsive typography.

The 13 summary rows in paper pages use a restrained rainbow accent sequence only for structure; the Home page uses a neutral single-color style.

## Notes On Accuracy

The summaries are intended as structured research-reading notes and should be checked against the original papers for citation-critical work.

When public code, dataset, project, benchmark, checkpoint, or PDF links could not be verified, the relevant field is marked with wording such as "확인되지 않음", "논문 내 명시 없음", or "공개 링크 확인 안 됨".

The English edition was machine translated from the existing Korean notes using Google Translate on November 16, 2026, with corrections to interface wording and detected translation omissions. It is not a fresh literature review or an independently verified translation of each original paper. Each page includes a translation notice. Technical wording, results, and resource availability should be checked against the original papers; the original ranking and citation snapshot is unchanged.

## Maintain And Validate

The root HTML files remain the Korean source. Update their notes and the corresponding entries in `translations/en.json`, then rebuild both editions:

```sh
python -m pip install -r scripts/requirements.txt
python scripts/build_bilingual.py
python scripts/validate_bilingual.py
python -m http.server 8000
```

Open `http://localhost:8000/` and verify the controls and page navigation in a browser. Building and reading the published pages do not contact a translation service or require an API key. Python and Beautiful Soup are only needed to maintain and validate the bundle; the published pages are static HTML. No user data is sent by the language controls; the preference is stored locally in the browser when permitted.

## Edition History

- [Original Korean bundle](https://github.com/gisbi-kim/robopaper-top500-13q/commit/f2722ec): The full 500-paper collection and ten 50-paper pages.
- **Bilingual edition — November 16, 2026:** Adds complete static English pages, a language selector on every page, remembered language preferences, and offline generation and validation. The English edition is a parallel translation of the Korean notes, not an updated paper-ranking snapshot.

## Citation

If you use this reading bundle, please cite or link both this repository and the original RoboPaper Atlas source.

```text
RoboPaper Top-500 13Q
https://gisbi-kim.github.io/robopaper-top500-13q/

RoboPaper Atlas
https://gisbi-kim.github.io/robopaper-atlas/index.html
```
