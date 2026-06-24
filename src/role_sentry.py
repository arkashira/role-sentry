import json
from dataclasses import dataclass
from typing import List

@dataclass
class Batch:
    transaction_id: int
    changes: List[str]

class RoleSentry:
    def __init__(self):
        self.batches = []
        self.max_batches = 5

    def record_batch(self, transaction_id: int, changes: List[str]):
        batch = Batch(transaction_id, changes)
        self.batches.append(batch)
        if len(self.batches) > self.max_batches:
            self.batches.pop(0)

    def undo_last_batch(self):
        if not self.batches:
            raise ValueError("No batches to undo")
        last_batch = self.batches.pop()
        return last_batch

    def get_last_batches(self):
        return self.batches[-self.max_batches:]

    def revert_changes(self, batch: Batch):
        # Revert changes made in the batch
        # This is a placeholder for the actual reversion logic
        return [f"Reverted {change}" for change in batch.changes]
