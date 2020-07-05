class Profile:
    def __init__(player, name, avatar, favGame, gameStats, gameHistory, friends, settings):
        player.name = name
        player.avatar = avatar
        player.favGame = favGame
        player.gameStats = gameStats
        player.gameHistory = gameHistory
        player.friends = friends
        player.settings = settings

    def printPlayer(player):
        print("Player Name: " + str(player.name) +
              "\n" + str(player.name) + "'s Avatar: " + str(player.avatar) +
              "\n" + str(player.name) + "'s Favorite Game: " + str(player.favGame) +
              "\n" + str(player.name) + "'s Game Stats: " + str(player.gameStats) +
              "\n" + str(player.name) + "'s Game History: " + str(player.gameHistory) +
              "\n" + str(player.name) + "'s Friends List: " + str(player.friends) +
              "\n" + str(player.name) + "'s Settings: " + str(player.settings))


p1 = Profile("Gio", "Default Photo", "Spades", "[Insert Game Statistics]",
             "[Insert Game History]", "[Insert Friends List]", "[Insert Settings]")

p1.printPlayer()
