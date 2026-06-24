from typing import Dict, List

class RefactorPlan:
    def __init__(self, role_name: str, steps: List[str]):
        self.role_name = role_name
        self.steps = steps

    def get_plan(self) -> Dict[str, str]:
        return {"role_name": self.role_name, "steps": "\n".join(self.steps)}

def create_refactor_plan(role_name: str, steps: List[str]) -> RefactorPlan:
    return RefactorPlan(role_name, steps)
