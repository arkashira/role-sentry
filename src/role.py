from dataclasses import dataclass
from enum import Enum
from typing import List

class RefactorStatus(Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    COMPLETED = 3

@dataclass
class Role:
    name: str
    size: int
    refactor_status: RefactorStatus

class RoleSentry:
    def __init__(self):
        self.roles = [
            Role("Role 1", 10, RefactorStatus.NOT_STARTED),
            Role("Role 2", 20, RefactorStatus.IN_PROGRESS),
            Role("Role 3", 30, RefactorStatus.COMPLETED),
        ]

    def get_roles(self) -> List[Role]:
        return self.roles

    def get_refactor_status(self, role_name: str) -> RefactorStatus:
        for role in self.roles:
            if role.name == role_name:
                return role.refactor_status
        return RefactorStatus.NOT_STARTED
