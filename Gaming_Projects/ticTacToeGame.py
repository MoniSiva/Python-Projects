"""
TIC TAC TOE GAME

addEntry() -> inserts the entry into the board at given position
isSpaceFree() -> checks whether the given position is free
displayBoard() -> displays the board's current status
isWinner() -> checks whether the user or computer has won by ordering the entries
playerTurn() -> gets the entry from the user
comparePositions() ->  compares the position and check whether user will win by next move so that computer can block the move
                       if no chance of winning for user, then will block random of possible position of
                       the free corner, middle and edges
selectRandomPosition()  -> picks the random position from possible moves passed by the comparePositions()
isBoardFull()  -> checks whether the board is full to decide the tie game.

"""
board = [' ' for x in range(10)]


def addEntry(letter, pos):
    board[pos] = letter


def isSpaceFree(pos):
    return board[pos] == ' '


def displayBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def playerTurn():
    play = True
    while play:
        position = input('It is your turn.\n Please select a position to place  \'X\' (1-9): ')
        try:
            position = int(position)
            if position > 0 and position < 10:
                if isSpaceFree(position):
                    play = False
                    addEntry('X', position)
                else:
                    print('Sorry, this space is already occupied!')
            else:
                print('Please type a number within the range (1-9) !')
        except:
            print('Please type only numbers of range(1-9) !')


def comparePositions():
    possiblePositions = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    position = 0

    for let in ['O', 'X']:
        for i in possiblePositions:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                position = i
                return position

    freeCorners = []
    for i in possiblePositions:
        if i in [1, 3, 7, 9]:
            freeCorners.append(i)

    if len(freeCorners) > 0:
        position = selectRandomPosition(freeCorners)
        return position

    if 5 in possiblePositions:
        position = 5
        return position

    freeEdges = []
    for i in possiblePositions:
        if i in [2, 4, 6, 8]:
            freeEdges.append(i)

    if len(freeEdges) > 0:
        position = selectRandomPosition(freeEdges)

    return position


def selectRandomPosition(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Welcome to Tic Tac Toe Game!')
    displayBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerTurn()
            displayBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not (isWinner(board, 'X')):
            move = comparePositions()
            if move == 0:
                print('Tie Game!')
            else:
                addEntry('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                displayBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')


while True:
    toProceed = input('Do you want to play again? (Y/N): ')
    if toProceed.lower() == 'y' or toProceed.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break