# ICLR submission package

## ⚠️ VENUE / DEADLINE CORRECTION (verified against iclr.cc + the live OpenReview API)

We have been calling this "ICLR 2026". **The ICLR 2026 cycle closed a year ago**
(abstracts 19 Sep 2025, papers 24 Sep 2025; the conference was held April 2026).
The cycle that is actually open is **ICLR 2027**:

| milestone | deadline (Anywhere on Earth) |
|---|---|
| **Abstract registration (MANDATORY)** | **Fri 18 Sep 2026, 11:59pm AoE** |
| Full paper PDF | Fri 25 Sep 2026, 11:59pm AoE |
| Reviews released | 5 Nov 2026 |
| Decisions | 16 Dec 2026 |

Abstract registration is **hard-enforced**: the OpenReview submission invitation itself
expires at the abstract deadline, so **no submission record can be created afterwards** —
missing it means we cannot submit the paper at all. Placeholder abstracts are deleted
(abstracts drive reviewer bidding), so the abstract must be genuine, which ours is.

**The PDF is optional at the abstract deadline** and is attached later via the per-paper
Revision button before the full-paper deadline. So 18 Sep needs only the fields below.

## Fields to paste into OpenReview (ready now)

**Title** (max 250 chars)
> Distribution Matching Is Not Task Preservation: Auditing Generative Models Inside Data Pipelines

**TL;DR** (optional, max 250 chars)
> Selecting a generative data transform by distributional similarity destroys task information; a frozen downstream model plus a no-learned-prior control exposes it cheaply.

**Keywords** (REQUIRED)
> distribution matching, generative model evaluation, downstream task utility, data-centric machine learning, synthetic data, distribution shift, evaluation protocols, domain adaptation

**Primary area** — suggest `datasets and benchmarks` (measurement/protocol paper);
`generative models` is the reasonable alternative. Pick from the live dropdown.

**Abstract** (REQUIRED, max 5000 chars — ours is ~197 words): see `abstract.txt`,
identical to the abstract compiled in `submission.pdf`.

**REFRAMED 2026-09-16 per advisor feedback:** the earlier abstract was rejected by Dr. Liu as
"too trivial and too much detail" and too image-specific for ICLR (risking mis-assigned
reviewers). The current version is general (generative models in data pipelines; vision is the
testbed, not the subject), plain-language, 3 numbers instead of 12, and carries novelty via a
mechanism claim rather than a metric complaint.

## Before the FULL-PAPER deadline (25 Sep) — not needed for 18 Sep

- [x] **Anonymize — DONE.** Ported to the official ICLR 2027 template. Single source, two builds:
      `body.tex` holds all content; `main.tex` is the non-anonymous preprint build (for sharing with
      collaborators) and **`submission.tex` is the anonymous ICLR build** (`\iclrfinalcopy` left
      commented, so the template renders "Anonymous authors / Paper under double-blind review").
      Verified on the compiled `submission.pdf`: ICLR 2027 header present, "Anonymous authors" block
      present, and zero occurrences of author names, institutions, emails, or repo URLs.
      **Submit `submission.pdf`, never `main.pdf`.**
- [ ] Main text ≤ 9 pages (currently **6** — comfortable). References/appendices unlimited.
- [ ] All co-authors need OpenReview profiles. **No authors may be added or removed after the
      abstract deadline** — so Dr. Liu must be on the record by 18 Sep.
- [ ] Reciprocal reviewing: one author must be nominated to register as a reviewer.
- [ ] LLM-usage disclosure (multi-select); non-disclosure of significant use risks desk reject.
- [ ] Checkboxes: code of ethics, submission guidelines, no-acknowledgements, no identity-revealing URL.
- [ ] Do NOT put the GitHub repo link in the submission (breaks anonymity); use an anonymized
      repo if we want to ship code, and it must not track visitors.

## Status of the work itself

Complete and publication-grade: both generative families (CycleGAN + SDEdit), the N=1000
three-seed frontier, the empty-prompt ablation, the ControlNet structure-preserving baseline,
both domains, 2 figures + 2 tables, compiling 6-page paper, reproducibility packet, green CI.
