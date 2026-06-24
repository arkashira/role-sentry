# Role Sentry

A tool for managing batches of changes and providing an undo feature.

## Usage

1. Create a `RoleSentry` instance.
2. Record batches of changes using `record_batch`.
3. Undo the last batch using `undo_last_batch`.
4. Get the last batches using `get_last_batches`.
5. Revert changes made in a batch using `revert_changes`.
