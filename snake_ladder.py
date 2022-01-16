import random

Snake_bite = {
    14:4,
    20:2,
    36:16,
    96:12
}

# Player class
class Player:
    def __init__(self, inPlayerNum):
        self.playerPos = 2
        self.playerNum = inPlayerNum

    def updatePosition(self, inPos):
        self.playerPos = inPos

    def getPosition(self):
        return self.playerPos

    def getPlayerNum(self):
        return self.playerNum


# Function to handle the players turn
def gameMaster(inPlayer):
    global winner
    # check for game winner
    if inPlayer.getPosition() == 100:
            print("Player %i is the Winner!" % inPlayer.getPlayerNum())
            winner = True

    # run dice rolls and movements
    if winner == False:
        print("\n----Player %i Hit enter to roll----" % inPlayer.getPlayerNum())
        # Uncomment to require space to be pressed before jumping turns
        # input()
        roll = rollDice()
        print("You rolled: %i" % roll)
        movePlayer(inPlayer, roll)
        checkPosition(inPlayer)


# Function to return the Integer value of a 6 side dice roll
def rollDice():
    result = random.choice((2, 4, 6))
    return result


# Handle player movements
def movePlayer(inPlayer, roll):
    if inPlayer.getPosition() + roll <= 100:
        inPlayer.updatePosition(inPlayer.getPosition() + roll)
        print("You are at spot %i" % inPlayer.getPosition())
    else:
        print("You rolled too far")


# Checks player landing position and adjusts if snake or ladder
def checkPosition(inPlayer):
    for pos in Snake_bite:
        if pos == inPlayer.getPosition():
            if pos < Snake_bite[pos]:
                print("You climbed a Ladder to spot %i" % Snake_bite[pos])
            else:
                print("You rode a Snake to spot %i" % Snake_bite[pos])
            inPlayer.updatePosition(Snake_bite[pos])


# Program entrance
if __name__ == '__main__':
    global winner
    winner = False
    numPlayers = int(input('Enter number of players: '))
    Player_name = input("Enter the player name:")
    playerList = []
    
    for i in range(0,numPlayers):
        playerList.append(Player(i))
        
    while winner == False:
        for i in playerList:
            if winner == False:
                gameMaster(i)





# import random
# def roll_dice():
#     result = random.choice(2, 4, 6)
#     return result
# board_size = int(input("enter size of the board: "))
# no_of_players = int(input("enter number of players wants to join: "))
# player_name = input("enter player name of 01: ")
# print("Welcome {} ".format(player_name))
# bite_positions = {
#     10: 1,
#     14: 4,
#     }
# current_position = 0
# decision = "y"
# while (decision == "y"):
#     decision = input("press y to continue OR n to quit the game: ")
#     if decision == "n":
#         break
#     current_position += roll_dice()
#     if current_position in bite_positions:


# Snakes and Ladders dictionary
# SaLdic = {6: 17,
#           14: 3,
#           20: 15,
#           24: 26,
#           30: 44,
#           39: 33,
#           49: 62,
#           66: 53,
#           69: 58,
#           79: 67,
#           82: 86,
#           84: 71,
#           88: 36,
#           }
