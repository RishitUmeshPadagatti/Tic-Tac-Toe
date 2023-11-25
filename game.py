def printingBoard(board):
    print("\n\n")
    print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
    print('_._._')
    print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
    print('_._._')
    print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])
    print()
def rememberPosition():
    pBoard=[['1','2','3'],['4','5','6'],['7','8','9']]
    print("Remember these positions")
    printingBoard(pBoard)
def updating(turn,pos):
    global board
    if pos==1: board[0][0]=turn
    elif pos==2: board[0][1]=turn
    elif pos==3: board[0][2]=turn
    elif pos==4: board[1][0]=turn
    elif pos==5: board[1][1]=turn
    elif pos==6: board[1][2]=turn
    elif pos==7: board[2][0]=turn
    elif pos==8: board[2][1]=turn
    elif pos==9: board[2][2]=turn
def swapping():
    global turn
    if turn=='x': turn='o'
    elif turn=='o': turn='x'
def checkingHorizontally(board):
    tempVar=0
    for row in board:
        if row==[turn,turn,turn]:
            tempVar+=1
    if tempVar>0:
        return True
    else:
        return False    
def checkingVertically(board):
    transpose=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in range(3):
        for j in range(3):
            transpose[i][j]=board[j][i]
    
    tempVar=0
    for row in transpose:
        if row==[turn,turn,turn]:
            tempVar+=1
    if tempVar>0:
        return True
    else:
        return False
def checkingDiagonally(board):
    diagonal1=[board[0][0], board[1][1], board[2][2]]
    diagonal2=[board[0][2], board[1][1], board[2][0]]
    tempTurn = [turn, turn, turn]
    if (diagonal1==tempTurn or diagonal2==tempTurn):
        return True
    else:
        return False
def checkingForWin():
    if checkingHorizontally(board)==True:
        return True
    elif checkingVertically(board)==True:
        return True
    elif checkingDiagonally(board)==True:
        return True
    else:
        return False


board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
rememberPosition()
turn='x'
positions=[]
for i in range(9):
    printingBoard(board)
    print("It is "+turn+"'s turn")
    pos=int(input("Enter position: "))
    if pos not in positions: positions.append(pos)
    else: 
        print("Already used")
        break
        
    if (pos>=1 and pos<=9): updating(turn,pos)
    else: break
    
    if checkingForWin()==True:
        printingBoard(board)
        print(turn+" WON!!!")
        break
    else:
        swapping()