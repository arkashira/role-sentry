import pytest
from src.role import RoleSentry, Role, RefactorStatus

def test_get_roles():
    sentry = RoleSentry()
    roles = sentry.get_roles()
    assert len(roles) == 3
    assert roles[0].name == "Role 1"
    assert roles[0].size == 10
    assert roles[0].refactor_status == RefactorStatus.NOT_STARTED

def test_get_refactor_status():
    sentry = RoleSentry()
    status = sentry.get_refactor_status("Role 1")
    assert status == RefactorStatus.NOT_STARTED
    status = sentry.get_refactor_status("Non-existent Role")
    assert status == RefactorStatus.NOT_STARTED
