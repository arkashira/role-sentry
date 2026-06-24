import pytest
from src.refactor import create_refactor_plan

def test_create_refactor_plan():
    plan = create_refactor_plan("Role 1", ["Step 1", "Step 2", "Step 3"])
    assert plan.get_plan()["role_name"] == "Role 1"
    assert plan.get_plan()["steps"] == "Step 1\nStep 2\nStep 3"
