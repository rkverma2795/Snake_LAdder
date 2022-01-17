import random

Snake_bite = {
    14:4,
    20:2,
    24:48,
    36:16,
    56:88,
    96:12
}
   

# Player class
class Player():
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
    if inPlayer.getPosition() == size_of_board:
            print("Player %s is the Winner!" % Player_name)
            winner = True

    # run dice rolls and movements
    if winner == False:
        print("\n----Player %s Hit enter to roll----" % Player_name)
        # Uncomment to require space to be pressed before jumping turns
        # input()
        roll = rollDice()
        print("Player rolled: %i" % roll)
        movePlayer(inPlayer, roll)
        checkPosition(inPlayer)


def rollDice():
    """
    even number on dice
    """
    result = random.choice((2, 4, 6))
    return result


# Handle player movements
def movePlayer(inPlayer, roll):
    if inPlayer.getPosition() + roll <= size_of_board:
        inPlayer.updatePosition(inPlayer.getPosition() + roll)
        print("Player %s at spot %i" % (Player_name,inPlayer.getPosition()))
    else:
        print("Player %s rolled too far" % Player_name)


# Checks player landing position and adjusts if snake or ladder
def checkPosition(inPlayer):
    for pos in Snake_bite:
        if pos == inPlayer.getPosition():
            if pos < Snake_bite[pos]:
                print("Ya hoooo climbed a Ladder to spot %i" % Snake_bite[pos])
            else:
                print("OOPS!!!!! SNAKE BITE, moved to  :  %i" % Snake_bite[pos])
            inPlayer.updatePosition(Snake_bite[pos])


# Program entrance
if __name__ == '__main__':
    global winner
    winner = False
    size_of_board = int(input("Enter the size of board: "))
    numPlayers = int(input('Enter number of players: '))
    Player_name = input("Enter the player name 01:")
    playerList = []
    
    for i in range(0,numPlayers):
        playerList.append(Player(i))
        
    while winner == False:
        for i in playerList:
            if winner == False:
                gameMaster(i)
