# SHARP-WAM: Sparse Hierarchical Attention with Probe Tokens for Bounded-Context World Action Modeling

[<img src="https://img.shields.io/badge/Project-SHARP--WAM-blue">](https://cham-0624.github.io/SHARP-WAM.github.io/) [<img src="https://img.shields.io/badge/License-MIT-green.svg">](LICENSE)

[English](README.md) | [中文](README_zh.md)

SHARP-WAM is a bounded-context world action model built around learnable probe tokens, a fixed-capacity KV set, and hierarchical sparse attention.

## Project Page

https://cham-0624.github.io/SHARP-WAM.github.io/

## Contents

```text
SHARP-WAM/
├── configs/
│   ├── train/                       # Training configuration
│   └── eval/                        # RMBench evaluation configuration
├── scripts/run.py
├── src/sharp_wam/models/
│   ├── probe_tokens.py
│   ├── hierarchical_attention.py
│   └── unified_kv_set.py
└── experiments/rmbench/
```

## Setup

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL> SHARP-WAM
cd SHARP-WAM
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Install RMBench and its data following their official instructions. Set `dataset_root` and a writable `output_dir` in the selected YAML file.

## Training

```bash
python scripts/run.py train \
  --config configs/train/rmbench_sharp_wam.yaml \
  --dataset-root /path/to/RMBench-LeRobot \
  --output-dir /path/to/output
```

To resume training:

```bash
python scripts/run.py train \
  --config configs/train/rmbench_sharp_wam.yaml \
  --dataset-root /path/to/RMBench-LeRobot \
  --resume /path/to/previous_checkpoint.pt
```

## Evaluation

Set `checkpoint`, `dataset_root`, and `task_name` in `configs/eval/rmbench.yaml`, then run:

```bash
python scripts/run.py eval \
  --config configs/eval/rmbench.yaml \
  --checkpoint /path/to/checkpoint.pt \
  --task-name press_button
```

## Availability

Training and inference code, model checkpoints, data preparation tools, and RMBench evaluation scripts will be released progressively. This repository will provide episode manifests, alignment tools, and simulator-specific calibration.

## TODO

- [ ] Release training code
- [ ] Release inference code
- [ ] Release model checkpoints
- [ ] Release data preparation tools
- [ ] Release RMBench evaluation scripts
- [ ] Add installation instructions
- [ ] Add real-robot deployment instructions
