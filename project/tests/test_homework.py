import pytest
from homeworks.homework16 import Player, Team

@pytest.fixture
def team():
    return Team("Real Madrid")

@pytest.fixture
def sample_players():
    return [
        Player("Messi", 10),
        Player("Ronaldo", 7),
        Player("Mbappe", 9)
    ]

class TestTeam:

    @pytest.mark.parametrize("name, number", [
        ("Neymar", 10),
        ("Lewandowski", 9)
    ])
    def test_add_player_param(self, team, name, number):
        player = Player(name, number)
        team.add_player(player)
        players_list = team.list_players()
        assert str(player) in players_list

    def test_remove_player(self, team, sample_players):
        for player in sample_players:
            team.add_player(player)

        team.remove_player(7)
        numbers = [int(p.split("#")[1].strip(")")) for p in team.list_players()]
        assert 7 not in numbers
        assert 10 in numbers and 11 in numbers

    def test_list_players(self, team, sample_players):
        for player in sample_players:
            team.add_player(player)
        players_list = team.list_players()
        expected = ["Messi (#10)", "Ronaldo (#7)", "Mbappe (#9)"]
        assert players_list == expected
