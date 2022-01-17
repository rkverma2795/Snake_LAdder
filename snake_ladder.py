import random

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


def crooked_dice():
    user_input = input("Do you want to enter snake moves(Y/N): ")
    print(user_input)
    user_input = user_input.lower()
    Snake_bite = {}
    if user_input == 'y':
        no_of_move = int(input('Enter Number of moves :'))
        print("Enter %i move" % no_of_move)
        for i in range(no_of_move):
            key, value = input().split()
            Snake_bite[key] = value
        return Snake_bite
    elif user_input == 'n':
        return Snake_bite
    else:
        print("Please type Y/N:")

    Snake_bite = "{"+", ".join(["{}:{}".format(k,v) for k,v in Snake_bite.items()])+"}"
    return  Snake_bite


def rollDice():
    """
    even number on dice
    """
    result = random.choice((2, 4, 6))
    return result


def crooked_dice():
    user_input = input("Do you want to enter snake moves(Y/N): ")
    if user_input.lower() == 'yes' or 'Y' or 'y':
        Snake_bite = {}
        no_of_move = int(input('Enter Number of moves :'))
        print("Enter {} move".format(no_of_move))
        for i in range(no_of_move):
            key, value = input().split()
            Snake_bite[key] = value

    else:
        Snake_bite = {}
    Snake_bite = "{"+", ".join(["{}:{}".format(k,v) for k,v in Snake_bite.items()])+"}"
    return  Snake_bite
    
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
    Snake_bite = crooked_dice()
    print(Snake_bite)
    playerList = []
    
    for i in range(0,numPlayers):
        playerList.append(Player(i))
        
    while winner == False:
        for i in playerList:
            if winner == False:
                gameMaster(i)
