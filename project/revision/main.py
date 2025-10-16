from homeworks.homework16 import Player, Team

def main():
    team = Team("Real Madrid")
    team.add_player(Player("Messi", 10))
    team.add_player(Player("Ronaldo", 7))
    print("Список гравців:", team.list_players())
    team.remove_player(10)
    print("Після видалення:", team.list_players())



if __name__ == "__main__":
    main()
