from dataclasses import dataclass
from typing import List

@dataclass
class AuditLog:
    timestamp: str
    action: str
    role_name: str

class AuditLogger:
    def __init__(self):
        self.logs = []

    def log_action(self, action: str, role_name: str) -> None:
        self.logs.append(AuditLog("now", action, role_name))

    def get_logs(self) -> List[AuditLog]:
        return self.logs
