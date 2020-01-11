#Sudoku
import numpy
archivo=input('Nombre del archivo con la matriz: ')
matriz=numpy.loadtxt(archivo,dtype=int)
validez='Matriz valida'
for row in matriz:
    suma=numpy.sum(row)
    if (suma!=45):
        validez='Matriz no valida'
for column in matriz:
    suma=numpy.sum(column)
    if (suma!=45):
        validez='Matriz no valida'     
print(validez)
