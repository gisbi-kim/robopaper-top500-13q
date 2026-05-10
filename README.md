# RoboPaper Top-500 13Q

Structured summaries of the top-cited robotics papers from RoboPaper Atlas, organized with a 13-question insight framework.

Live site: https://gisbi-kim.github.io/robopaper-top500-13q/

## What This Is

This repository publishes a self-contained HTML reading bundle for 500 highly cited robotics papers from the RoboPaper Atlas paper explorer.

Each paper card is summarized in Korean using 13 fixed research-reading questions:

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

The older local Google-style export is intentionally not part of the published bundle.

## Design

The pages use a bright, restrained Apple-style layout with large paper cards, single-column summary rows, subtle shadows, rounded corners, and responsive typography.

The 13 summary rows in paper pages use a restrained rainbow accent sequence only for structure; the Home page uses a neutral single-color style.

## Notes On Accuracy

The summaries are intended as structured research-reading notes and should be checked against the original papers for citation-critical work.

When public code, dataset, project, benchmark, checkpoint, or PDF links could not be verified, the relevant field is marked with wording such as "확인되지 않음", "논문 내 명시 없음", or "공개 링크 확인 안 됨".

## Citation

If you use this reading bundle, please cite or link both this repository and the original RoboPaper Atlas source.

```text
RoboPaper Top-500 13Q
https://gisbi-kim.github.io/robopaper-top500-13q/

RoboPaper Atlas
https://gisbi-kim.github.io/robopaper-atlas/index.html
```
