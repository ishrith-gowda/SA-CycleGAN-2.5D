# per-class IoU by condition (N=1000, frozen SegFormer-b4)

| class | raw | colormatch | cyclegan | sdedit_0.50 | controlnet | rel. drop (SDEdit 0.50) |
|---|---|---|---|---|---|---|
| road | 0.937 | 0.932 | 0.843 | 0.845 | 0.884 | 10% |
| sidewalk | 0.540 | 0.502 | 0.202 | 0.280 | 0.309 | 48% |
| building | 0.711 | 0.681 | 0.356 | 0.504 | 0.505 | 29% |
| wall | 0.356 | 0.315 | 0.089 | 0.077 | 0.094 | 78% |
| fence | 0.102 | 0.111 | 0.020 | 0.021 | 0.031 | 79% |
| pole | 0.269 | 0.252 | 0.112 | 0.095 | 0.159 | 65% |
| traffic light | 0.073 | 0.067 | 0.008 | 0.008 | 0.012 | 90% |
| traffic sign | 0.069 | 0.063 | 0.012 | 0.017 | 0.022 | 76% |
| vegetation | 0.649 | 0.625 | 0.364 | 0.455 | 0.427 | 30% |
| terrain | 0.227 | 0.159 | 0.083 | 0.050 | 0.011 | 78% |
| sky | 0.901 | 0.883 | 0.121 | 0.750 | 0.755 | 17% |
| person | 0.270 | 0.240 | 0.035 | 0.024 | 0.111 | 91% |
| rider | 0.182 | 0.156 | 0.028 | 0.015 | 0.085 | 92% |
| car | 0.737 | 0.725 | 0.384 | 0.226 | 0.447 | 69% |
| truck | 0.666 | 0.608 | 0.198 | 0.197 | 0.175 | 70% |
| bus | 0.248 | 0.259 | 0.206 | 0.097 | 0.127 | 61% |
| train | 0.002 | 0.002 | 0.000 | 0.001 | 0.001 | 62% |
| motorcycle | 0.279 | 0.303 | 0.101 | 0.016 | 0.046 | 94% |
| bicycle | 0.008 | 0.007 | 0.001 | 0.001 | 0.004 | 92% |

## grouped (classes with raw IoU >= 0.05 only)

| group | raw | colormatch | cyclegan | sdedit_0.50 | controlnet |
|---|---|---|---|---|---|
| large regions | 0.661 | 0.630 (-5%) | 0.328 (-50%) | 0.481 (-27%) | 0.482 (-27%) |
| thin / small objects | 0.174 | 0.168 (-4%) | 0.052 (-70%) | 0.030 (-83%) | 0.065 (-63%) |

**reading:** the non-learned control degrades both groups mildly and almost uniformly; every learned translation degrades thin/small label-carrying objects far more than large amorphous regions. the learned prior repaints plausible large regions while destroying the fine structure the frozen segmenter relies on.
