"""Fixed-capacity key-value set interface."""

from __future__ import annotations

from typing import Any


class UnifiedKVSet:
    """Maintains a bounded set of historical key-value states."""

    def __init__(self, capacity: int = 0) -> None:
        self.capacity = capacity

    def update(self, entry: Any) -> None:
        """Add an entry and apply the retention policy."""
        raise NotImplementedError("UnifiedKVSet.update is not released yet.")
