board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentPlayer = "X"
winner = None
gameRunning = True

#Affiche le tableau

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

#Le joueur choisit une case
def playerInput(board):
    while True:
        if currentPlayer == "X":
            inp = int(input(f"Enter un nombre 1-9 \033[1;34m Joueur (X) \033[0;0m : "))
        else:
            inp = int(input(f"Enter un nombre 1-9 \033[1;31m Joueur (O) \033[0;0m : "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer
            break
        else:
            if currentPlayer == "X":
                print(f"Attention! La case est prise \033[1;34m Joueur (X) \033[0;0m ! ")
            else:
                print(f"Attention! La case est prise \033[1;31m Joueur (O) \033[0;0m ! ")
            printBoard(board)


#Vérifie si un joueur a gagné ou une égalité
def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer
        return True

def checkVertical(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer
        return True

def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[8] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("C'est une égalité")
        gameRunning = False

def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print(f"Le gagnant est {winner}")

#Changement de joueur
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"



#Vérifie si un joueur a gagné ou une égalité

while gameRunning:
    printBoard(board)
    if winner != None:
        break
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()