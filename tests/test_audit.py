import pytest
from src.audit import AuditLogger, AuditLog

def test_audit_logger():
    logger = AuditLogger()
    logger.log_action("Refactor", "Role 1")
    logger.log_action("Delete", "Role 2")
    logs = logger.get_logs()
    assert len(logs) == 2
    assert logs[0].timestamp == "now"
    assert logs[0].action == "Refactor"
    assert logs[0].role_name == "Role 1"
    assert logs[1].timestamp == "now"
    assert logs[1].action == "Delete"
    assert logs[1].role_name == "Role 2"
