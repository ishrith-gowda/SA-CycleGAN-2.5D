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
> Fidelity Is Not Utility: A Controlled Dissociation in Learned Image Translation

**TL;DR** (optional, max 250 chars)
> Under a frozen downstream evaluator, learned image translation buys FID by destroying task utility — across a GAN and a diffusion model, in driving and medical MRI; non-learned baselines do not.

**Keywords** (REQUIRED)
> image-to-image translation, evaluation of generative models, FID, downstream utility, domain adaptation, diffusion models, medical image harmonization, semantic segmentation

**Primary area** — suggest `datasets and benchmarks` (this is a measurement/protocol paper);
`generative models` is the reasonable alternative. Pick from the live dropdown.

**Abstract** (REQUIRED, max 5000 chars — ours is ~1.8k chars / 269 words): see `abstract.txt`,
identical to the abstract compiled in `main.pdf`.

## Before the FULL-PAPER deadline (25 Sep) — not needed for 18 Sep

- [ ] **Anonymize.** Port from `arxiv.sty` to the official ICLR template (the template renders
      "Anonymous authors / Paper under double-blind review" unless the final-copy flag is set).
      The ONLY hazard in our source is the author block at `main.tex` lines 18-25 — verified: no
      GitHub/repo URLs, no acknowledgements section, Reproducibility Statement leaks nothing.
      **Author identity in text or supplement = desk reject.**
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
