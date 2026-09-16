"""Hierarchical sparse-attention interface."""

from __future__ import annotations

from typing import Any


class HierarchicalSparseAttention:
    """Selects bounded historical context for attention."""

    def __init__(self, max_frames: int = 0, max_tokens_per_frame: int = 0) -> None:
        self.max_frames = max_frames
        self.max_tokens_per_frame = max_tokens_per_frame

    def forward(self, queries: Any, memory: Any) -> Any:
        """Apply hierarchical sparse attention to the current queries."""
        raise NotImplementedError("HierarchicalSparseAttention.forward is not released yet.")
