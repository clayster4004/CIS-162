"""Project 2 - Word Tac Toe

Clay Beal - 11/2/2022
Word Tic-Tac-Toe, a game that tries to match the second letter of 
each word in a row to win the game.

I certify that this work was done in accordance with
GV academic honesty policies.

Fall, 2022"""

def printBoard(b):
    '''This function prints out the board with words added as they are inputted'''
    count = 0
    print('----------------------') # Top of board
    for i in b:
        if i == '':
            print('|' + '   ' + i + '   ', end='') # Makes a tab space for each potential spot
            count += 1
        else:
            print(f'| {i} ', end='')
            count += 1

        if count % 3 == 0: # After three spots made, goes to next line
            print('|', end='')
            print()
            print('----------------------') #Bottom of board


def chooseWord(words, used, word):
    '''This function checks to see if the word is available / in the list
       it appends the word to a used list if used and removes it from the available list'''
    # Checks to see if the user inputted word is in the word list
    if word not in words:
        return False
    # If it is the word is removed from the list and put on the used list
    else:
        used.append(word)
        words.remove(word)
        return True # So the game can continue


def checkRows(b):
    '''Checks to see if any of the three rows have three in a row (win)'''
    i = 0
    # Checks to see if the spots have words in them, if not skips over the row
    while i < 9:
        if b[i] != '' and b[i+1] != '' and b[i+2] != '':
            # Checks to see if the second letter is the same in all the words
            if b[i][1] == b[i+1][1] and b[i][1] == b[i+2][1]:
                return True
            # Adds 3 to i bringing it to the start of the next row
            else:
                i+=3
        else:
            i+=3
    # Returns False if no win condition is met
    return False


def checkCols(b):
    '''Checks to see if any of the three columns have three in a row (win)'''
    i = 0
    while i < 3:
        # Checks to see if all the slots in the column have words in them
        if b[i] != '' and b[i+3] != '' and b[i+6] != '':
            # Checks to see if the second letter is the same in all the words
            if b[i][1] == b[i+3][1] and b[i][1] == b[i+6][1]:
                return True
            # Adds 1 to i bringing it to the start of the next column
            else:
                i+=1
        else:
            i+=1
    # None of the win conditions met, returns false
    return False


def checkLeftDiag(b):
    '''Checks if left diagonal has three in a row (win)'''
    # Checks if the spots have words in them
    if b[0] != '' and b[4] != '' and b[8] != '':
        # Checks if they all have the same second letter
        if b[0][1] == b[4][1] and b[0][1] == b[8][1]:
            return True
        # Returns False if the win condition is not met / doesn't have words in slots
        else:
            return False
    else:
        return False


def checkRightDiag(b):
    '''Checks to see if right diagonal has three in a row (win)'''
    # Checks if the spots have words in them
    if b[2] != '' and b[4] != '' and b[6] != '':
        # Checks if they all have the same second letter
        if b[2][1] == b[4][1] and b[2][1] == b[6][1]:
            return True
        # Returns False if the win condition is not met / doesn't have words in slots
        else:
            return False
    else:
        return False


board = [ "" for i in range(0,9) ] # Creates list with 9 slots

# Word list for game and empty list to hold used words
words = ["jump", "stunt", "apple", "raft", "snow", "sheep", "moon", "small", "sword"]
used = []

player = 1 # Keeps track of whose turn it is in the game, resets at end

gameOver = False # Variable setting gameOver to False, only changes if a win is detected

# Game will continue until a win is detected
while not gameOver:
    # Variables to hold user inputted word and position they want to place word
    word = ''
    position = ''

    # Will be true everytime the loop resets
    while word == '':
        # Prints board and list of remaining words
        printBoard(board)
        print(words)
        print()

        # Prints who's turn it is to select a word
        word = input(f'Player {player}\'s turn to choose a word -> ')
        print()

        # Checks to see if user input is valid through the chooseWords function
        while not (chooseWord(words, used, word)):
            #Asks user to retype a word everytime the input is invalid
            word = input(f'Player {player}\'s turn to choose a word -> ')
            print()

        # Asks user where they'd like to place the word
        position = input('Which position would you like to place your word "0-8" -> ')
        print()

    # Will always run until loop is broken out of
    while True:
        # Asks for postion until it is a digit
        while not position.isdigit():
            position = input('Which position would you like to place your word -> ')
            print()

        # Converts position into an integer
        position = int(position)    
        # Checks if position is in the range and doesn't already have a word there
        # If it does, the loop will run again and ask for a new position
        if position not in range(0,9) or board[position] != '':
            position = ''
        # Runs if all conditions are met, puts word on the board and breaks out of loop
        else:
            board[position] = word
            break

    # Runs the functions to see if there is a win, if so main gameOver loop breaks        
    if checkRows(board) or checkCols(board) or checkLeftDiag(board) or checkRightDiag(board):
        gameOver = True
    # If no win player is flip-flopped and gameOver runs again
    else:
        if player == 1:
            player = 2
        else:
            player = 1

    if not words:
        print('It\'s a tie!')
        player = 'cat'
        break


# After gameOver is broken, the board is printed and the player who won is printed
printBoard(board)
print()
print(f'Player {player} wins!')


