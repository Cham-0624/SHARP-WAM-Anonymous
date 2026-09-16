"""Learnable probe-token interface."""

from __future__ import annotations

from typing import Any


class LearnableProbeTokens:
    """Summarizes observations into learnable probe tokens."""

    def __init__(self, num_probes: int = 8, hidden_dim: int = 0) -> None:
        self.num_probes = num_probes
        self.hidden_dim = hidden_dim

    def forward(self, visual_tokens: Any) -> Any:
        """Produce contextualized probe tokens from visual tokens."""
        raise NotImplementedError("LearnableProbeTokens.forward is not released yet.")
