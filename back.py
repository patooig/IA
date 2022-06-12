from random import randint
from time import sleep

#initialise empty 9 by 9 grid
matriz = []
matriz.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
matriz.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
matriz.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
matriz.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
matriz.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
matriz.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
matriz.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
matriz.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
matriz.append([0, 0, 5, 2, 0, 6, 3, 0, 0])


def printMatriz(matriz):
    for fila in range(0,9):
        for columna in range(0,9):
            print(matriz[fila][columna], end=" ")
        print()
    print()

#A function to check if the grid is full
def verificarMatriz(matriz):
  for fila in range(0,9):
      for columna in range(0,9):
        if matriz[fila][columna]==0:
          return False

  #We have a complete grid!  
  return True 

#A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def solveGrid(grid):
  #Find next empty cell
  for i in range(0,81):
    fila=i//9
    columna=i%9
    if grid[fila][columna]==0:
      for val in range (1,10):
        #Check that this value has not already be used on this row
        if not(val in grid[fila]):
          #Check that this value has not already be used on this column
          if not val in (grid[0][columna],grid[1][columna],grid[2][columna],grid[3][columna],grid[4][columna],grid[5][columna],grid[6][columna],grid[7][columna],grid[8][columna]):
            #Identify which of the 9 squares we are working on
            square=[]
            if fila<3:
              if columna<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif columna<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif fila<6:
              if columna<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif columna<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if columna<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif columna<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
            #Check that this value has not already be used on this 3x3 square
            if not val in (square[0] + square[1] + square[2]):
              grid[fila][columna]=val          
              if verificarMatriz(grid):
                print("Grid Complete and Checked")
                return True
              else:
                if solveGrid(grid):
                  return True
      break
  print("Backtrack")
  grid[fila][columna]=0  
  

sleep(1)

solved = solveGrid(matriz)
if solved:
  print("Sudoku tiene solucion")
else:  
  print("No se puede resolver el sudoku")

printMatriz(matriz)