#!/usr/bin/env python3
"""Launch SHARP-WAM training or RMBench evaluation."""

from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path


COMMAND_ENV = {
    "train": "SHARP_WAM_TRAIN_COMMAND",
    "eval": "SHARP_WAM_EVAL_COMMAND",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="SHARP-WAM launcher")
    parser.add_argument("mode", choices=sorted(COMMAND_ENV))
    parser.add_argument("--config", required=True, type=Path)
    args, overrides = parser.parse_known_args()
    args.overrides = overrides
    return args


def main() -> int:
    args = parse_args()
    if not args.config.is_file():
        raise FileNotFoundError(f"Configuration file not found: {args.config}")

    env_name = COMMAND_ENV[args.mode]
    command = os.environ.get(env_name)
    if not command:
        print(f"{env_name} is not configured.", file=sys.stderr)
        return 2

    child_command = shlex.split(command)
    if not child_command:
        raise ValueError(f"{env_name} must contain an executable command")
    child_command.extend(["--config", str(args.config.resolve()), *args.overrides])
    return subprocess.run(child_command, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
