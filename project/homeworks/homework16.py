class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name} (#{self.number})"


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, number):
        self.players = [player for player in self.players if player.number != number]

    def list_players(self):
        return [str(player) for player in self.players]




