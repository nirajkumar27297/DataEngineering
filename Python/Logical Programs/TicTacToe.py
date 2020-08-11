# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:01:37 2020

@author: Niraj Kumar
Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1
is the Computer and the Player 2 is the user. Player 1 take Random Cell that is
the Column and Row.
"""
import random;
def displayBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j],end = "|")
        print()
        print("------")
#if the space is already occupied then return False
def moveValid(board,move):
     if(board[(move // 3)][move % 3] != "X" and board[(move // 3)][move % 3] != "O"):
         return True 
     else:
         return False
#Computer play using random function
def computerMovePlay(board):
    while(1):
        move = random.randint(0,8)
        if(moveValid(board,move) == True):
            return move
def equals3(a, b, c):
    return (a == b and b == c)
def checkGameResult(board):
    winner = None;

    # horizontal
    for i in range(3):
          if (equals3(board[i][0], board[i][1], board[i][2])):
              winner =board[i][0]

    #Vertical
    for i in range(3):
          if (equals3(board[0][i], board[1][i], board[2][i])):
              winner =board[0][i]

    #Diagonal
    if (equals3(board[0][0], board[1][1], board[2][2])):
        winner = board[0][0]
    if (equals3(board[2][0], board[1][1], board[0][2])):
        winner =board[2][0];
           
    if (draw(board) and winner is None  ):
          return "tie";
    else:
        return winner
 #Checking for draw   
def draw(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j].isdigit()):
                return False
    return True
    
    

#main function
#board initialization
board = [['' for i in range(3)] for j in range(3)]
#Initialization of count variable
count = 1
for i in range(3):
    for j in range(3):
        board[i][j] = str(count) 
        count += 1
""""
1 - Player Turn
0 -Computer Turn
"""
turn = 1        
while(1):
    if(turn == 1):
        
        print("Player Chance to Play")
        displayBoard(board)
        playerMove = int(input("Enter the position"))
        playerMove -= 1
        if(not moveValid(board,playerMove)):
            print("invalid move Try one More time")
            continue;
        board[(playerMove // 3)][playerMove % 3] = 'X'
        displayBoard(board)
    elif(turn == 0):
    #Computer move
        print("Computer Chance to play")
        computerMove = computerMovePlay(board)
        print("Computer move is ",computerMove+1)
        board[(computerMove // 3)][computerMove % 3] = 'O'
        displayBoard(board)
    #Checking result
    checkResult = checkGameResult(board)
    if(checkResult is not None):
        if(checkResult == "X"):
            displayBoard(board)
            print("Winner is player")
        elif(checkResult == "O"):
            displayBoard(board)
            print("Winner is player")
        elif(checkResult == "tie"):
            displayBoard(board)
            print("Game is draw")
        break
    if(turn == 1):
        turn = 0
    else:
        turn = 1
    
            
    