from laxleague.guardian import Guardian
from laxleague.player import Player


def test_construction() -> None:
    p = Player("Tatiana", "Jones")
    assert "Tatiana" == p.first_name
    assert "Jones" == p.last_name
    assert [] == p.guardians


def test_add_guardian() -> None:
    g = Guardian("Mary", "Jones")
    p = Player("Tatiana", "Jones")
    p.add_guardian(g)
    assert [g] == p.guardians
