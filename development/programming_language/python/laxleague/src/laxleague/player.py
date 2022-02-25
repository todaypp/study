from dataclasses import dataclass
from dataclasses import field
from typing import List

from laxleague.guardian import Guardian


@dataclass
class Player:
    """A lacrosse player in the league"""

    first_name: str
    last_name: str
    guardians: List[Guardian] = field(default_factory=list)

    def add_guardian(self, guardian: Guardian) -> None:
        self.guardians.append(guardian)
