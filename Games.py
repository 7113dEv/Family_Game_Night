class gamesPlayed:
    def __init__(game, hearts, spades, ginRummy, klondike, triPeaks):
        game.heartsPlayed = hearts
        game.spadesPlayed = spades
        game.ginRummyPlayed = ginRummy
        game.klondikePlayed = klondike
        game.triPeaksPlayed = triPeaks


def showFavoriteGame(profileData):
    mostPlayed = [profileData[0]]

    for game in profileData:

        # If there are multiple games of the same amount played and a more played game is found
        if int(len(mostPlayed)) > 1 and game > mostPlayed[0]:
            # Delete all elements and add new most played game
            mostPlayed.clear()
            mostPlayed.append(game)

        if game > mostPlayed[0]:
            mostPlayed[0] = game
        elif game == mostPlayed[0]:
            mostPlayed.append(game)
