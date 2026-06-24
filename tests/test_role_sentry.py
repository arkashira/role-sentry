from role_sentry import RoleSentry, Batch

def test_record_batch():
    sentry = RoleSentry()
    sentry.record_batch(1, ["change1", "change2"])
    assert len(sentry.batches) == 1
    assert sentry.batches[0].transaction_id == 1
    assert sentry.batches[0].changes == ["change1", "change2"]

def test_undo_last_batch():
    sentry = RoleSentry()
    sentry.record_batch(1, ["change1", "change2"])
    sentry.record_batch(2, ["change3", "change4"])
    undone_batch = sentry.undo_last_batch()
    assert undone_batch.transaction_id == 2
    assert undone_batch.changes == ["change3", "change4"]
    assert len(sentry.batches) == 1

def test_get_last_batches():
    sentry = RoleSentry()
    sentry.record_batch(1, ["change1", "change2"])
    sentry.record_batch(2, ["change3", "change4"])
    sentry.record_batch(3, ["change5", "change6"])
    last_batches = sentry.get_last_batches()
    assert len(last_batches) == 3
    assert last_batches[0].transaction_id == 1
    assert last_batches[1].transaction_id == 2
    assert last_batches[2].transaction_id == 3

def test_revert_changes():
    sentry = RoleSentry()
    batch = Batch(1, ["change1", "change2"])
    reverted_changes = sentry.revert_changes(batch)
    assert reverted_changes == ["Reverted change1", "Reverted change2"]

def test_undo_last_batch_empty():
    sentry = RoleSentry()
    try:
        sentry.undo_last_batch()
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "No batches to undo"
