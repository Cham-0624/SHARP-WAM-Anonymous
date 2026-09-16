# SHARP-WAM：用于有界上下文世界动作建模的带探针 Token 稀疏层级注意力

[<img src="https://img.shields.io/badge/Project-SHARP--WAM-blue">](https://cham-0624.github.io/SHARP-WAM.github.io/) [<img src="https://img.shields.io/badge/License-MIT-green.svg">](LICENSE)

[English](README.md) | [中文](README_zh.md)

SHARP-WAM 是一个有界上下文世界动作模型，其正式设计包含可学习探针 Token、固定容量 KV 集和层级稀疏注意力。

## 项目主页

https://cham-0624.github.io/SHARP-WAM.github.io/

## 目录

```text
SHARP-WAM/
├── configs/
│   ├── train/                       # 训练配置
│   └── eval/                        # RMBench 评测配置
├── scripts/run.py
├── src/sharp_wam/models/
│   ├── probe_tokens.py
│   ├── hierarchical_attention.py
│   └── unified_kv_set.py
└── experiments/rmbench/
```

## 环境安装

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL> SHARP-WAM
cd SHARP-WAM
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

请按 RMBench 官方说明安装 benchmark 和数据集，并在所选 YAML 中填写 `dataset_root` 和可写的 `output_dir`。

## 训练

```bash
python scripts/run.py train \
  --config configs/train/rmbench_sharp_wam.yaml \
  --dataset-root /path/to/RMBench-LeRobot \
  --output-dir /path/to/output
```

恢复训练：

```bash
python scripts/run.py train \
  --config configs/train/rmbench_sharp_wam.yaml \
  --dataset-root /path/to/RMBench-LeRobot \
  --resume /path/to/previous_checkpoint.pt
```

## 评测

在 `configs/eval/rmbench.yaml` 中填写 `checkpoint`、`dataset_root` 和 `task_name`，然后执行：

```bash
python scripts/run.py eval \
  --config configs/eval/rmbench.yaml \
  --checkpoint /path/to/checkpoint.pt \
  --task-name press_button
```

## 发布计划

训练和推理代码、模型 checkpoint、数据准备工具和 RMBench 评测脚本将逐步发布。本仓库计划提供 episode manifest、对齐工具和特定模拟器校准。

## TODO

- [ ] 发布训练代码
- [ ] 发布推理代码
- [ ] 发布模型 checkpoint
- [ ] 发布数据准备工具
- [ ] 发布 RMBench 评测脚本
- [ ] 添加安装说明
- [ ] 添加真实机器人部署说明
