#!/usr/bin/env python3
"""per-class degradation analysis: WHICH classes learned translation destroys.

the headline mIoU collapse hides structure. this breaks it out per Cityscapes class and groups
classes into large amorphous regions (road, sky, building, ...) vs thin/small label-carrying
objects (poles, traffic lights/signs, riders, ...). the learned translations degrade the thin
classes far more than the large ones, while the non-learned control degrades both mildly and
almost uniformly -- evidence that the learned prior resynthesises plausible large regions while
obliterating the fine structure the segmenter depends on.

classes whose RAW IoU is below --min-iou are excluded from the grouped statistics: a relative
drop computed off a near-zero baseline is noise, not signal (e.g. train, bicycle in GTA5).

usage: per_class_analysis.py --results <dir> [--out <dir>] [--min-iou 0.05]
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import statistics

NAMES = [
    "road",
    "sidewalk",
    "building",
    "wall",
    "fence",
    "pole",
    "traffic light",
    "traffic sign",
    "vegetation",
    "terrain",
    "sky",
    "person",
    "rider",
    "car",
    "truck",
    "bus",
    "train",
    "motorcycle",
    "bicycle",
]
# large amorphous regions vs thin / small label-carrying objects (Cityscapes train ids)
LARGE = [0, 1, 2, 8, 9, 10]
THIN = [5, 6, 7, 12, 17, 18]


def _per_class(path: str) -> dict[str, float]:
    with open(path) as f:
        return json.load(f)["per_class_iou"]


def _mean_over_seeds(results: str, pattern: str) -> dict[str, float]:
    files = sorted(glob.glob(os.path.join(results, f"{pattern}.json")))
    if not files:
        return {}
    ds = [_per_class(p) for p in files]
    return {k: statistics.mean(d[k] for d in ds) for k in ds[0]}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--out", default="")
    ap.add_argument(
        "--min-iou",
        type=float,
        default=0.05,
        help="exclude classes whose raw IoU is below this from grouped stats",
    )
    a = ap.parse_args()
    out = a.out or a.results

    conds = {
        "raw": _per_class(os.path.join(a.results, "raw.json")),
        "colormatch": _per_class(os.path.join(a.results, "colormatch.json")),
        "cyclegan": _per_class(os.path.join(a.results, "cyclegan.json")),
        "sdedit_0.50": _mean_over_seeds(a.results, "sdedit_s50_seed*"),
        "controlnet": _mean_over_seeds(a.results, "controlnet_seed*"),
    }
    raw = conds["raw"]
    order = ["raw", "colormatch", "cyclegan", "sdedit_0.50", "controlnet"]

    md = [
        "# per-class IoU by condition (N=1000, frozen SegFormer-b4)",
        "",
        "| class | " + " | ".join(order) + " | rel. drop (SDEdit 0.50) |",
        "|---" * (len(order) + 2) + "|",
    ]
    for i, name in enumerate(NAMES):
        k = str(i)
        vals = [conds[c].get(k, float("nan")) for c in order]
        drop = (
            (raw[k] - conds["sdedit_0.50"].get(k, 0.0)) / raw[k] if raw[k] > 1e-6 else float("nan")
        )
        md.append(f"| {name} | " + " | ".join(f"{v:.3f}" for v in vals) + f" | {drop * 100:.0f}% |")

    def group_mean(idx: list[int], d: dict[str, float]) -> float:
        keep = [i for i in idx if raw[str(i)] >= a.min_iou]
        return statistics.mean(d[str(i)] for i in keep) if keep else float("nan")

    md += [
        "",
        f"## grouped (classes with raw IoU >= {a.min_iou} only)",
        "",
        "| group | " + " | ".join(order) + " |",
        "|---" * (len(order) + 1) + "|",
    ]
    summary = {}
    for label, idx in [("large regions", LARGE), ("thin / small objects", THIN)]:
        gv = [group_mean(idx, conds[c]) for c in order]
        base = gv[0]
        cells = [f"{gv[0]:.3f}"] + [f"{v:.3f} ({(v - base) / base * 100:+.0f}%)" for v in gv[1:]]
        md.append(f"| {label} | " + " | ".join(cells) + " |")
        summary[label] = {c: gv[j] for j, c in enumerate(order)}
    md += [
        "",
        "**reading:** the non-learned control degrades both groups mildly and almost uniformly; "
        "every learned translation degrades thin/small label-carrying objects far more than large "
        "amorphous regions. the learned prior repaints plausible large regions while destroying the "
        "fine structure the frozen segmenter relies on.",
    ]

    with open(os.path.join(out, "per_class_table.md"), "w") as f:
        f.write("\n".join(md) + "\n")
    with open(os.path.join(out, "per_class_summary.json"), "w") as f:
        json.dump(
            {
                "grouped": summary,
                "min_iou": a.min_iou,
                "per_class": {
                    NAMES[i]: {c: conds[c].get(str(i)) for c in order} for i in range(19)
                },
            },
            f,
            indent=2,
        )
    print("\n".join(md))
    print(f"\nwrote per_class_table.md / per_class_summary.json -> {out}")


if __name__ == "__main__":
    main()
