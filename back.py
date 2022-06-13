from random import randint
import time

matriz = [] #Matriz
result = []
#Abrir archivo
A=1
with open("sudoku.txt","r") as archivo:
    for linea in archivo:
      
      for i in range(0, len(linea)-1, A):
        result.append(int(linea[i : i + A]))

      matriz.append(result.copy())
      result.clear()


def printMatriz(matriz):
    for fila in range(0,9):
        for columna in range(0,9):
            print(matriz[fila][columna], end=" ")
        print()

#Verifica si existe un 0, si existe es pq matriz no tuvo soluciòn
def verificarMatriz(matriz):
  for fila in range(0,9):
      for columna in range(0,9):
        if matriz[fila][columna]==0:
          return False

  return True 

#BACKTRACCKING

#INICIO

def backtracking(m):
  for i in range(0,81):

    fila=i//9      #Divisiòn entera
    columna=i%9    #Resto de divisiòn
    
    if m[fila][columna]==0:

      for val in range (1,10,1):

        if not(val in m[fila]):
          aux = []
          for k in range(0,9,1):
            print(m[k][columna])
            aux.append(m[k][columna])

          if not val in (aux):
            #Identify which of the 9 squares we are working on
            grupo3x3=[]
            if fila<3:
              if columna<3:
                grupo3x3=[m[i][0:3] for i in range(0,3)]
              elif columna<6:
                grupo3x3=[m[i][3:6] for i in range(0,3)]
              else:  
                grupo3x3=[m[i][6:9] for i in range(0,3)]
            elif fila<6:
              if columna<3:
                grupo3x3=[m[i][0:3] for i in range(3,6)]
              elif columna<6:
                grupo3x3=[m[i][3:6] for i in range(3,6)]
              else:  
                grupo3x3=[m[i][6:9] for i in range(3,6)]
            else:
              if columna<3:
                grupo3x3=[m[i][0:3] for i in range(6,9)]
              elif columna<6:
                grupo3x3=[m[i][3:6] for i in range(6,9)]
              else:  
                grupo3x3=[m[i][6:9] for i in range(6,9)]
            #Check that this value has not already be used on this 3x3 square
            if not val in (grupo3x3[0] + grupo3x3[1] + grupo3x3[2]):
              m[fila][columna]=val          
              if verificarMatriz(m):
                print("")
                return True
              else:
                if backtracking(m):
                  return True
      break
  #Volver atràs
  m[fila][columna]=0  
  

#CÀLCULO TIEMPO DE EJECUCIÒN ALGORITMO DE BÙSQUEDA BACKTRACKING
start= time.time()
solved = backtracking(matriz)
end=time.time()
print("Tiempo backtracking: ",end-start)
  
if solved:
  print("Sudoku tiene solucion")
else:  
  print("No se puede resolver el sudoku")

printMatriz(matriz)