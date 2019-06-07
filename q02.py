##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##

import csv
file = open('data.csv', 'r')
filecsv = csv.reader(file, delimiter= '\t')
lista = list()
for x in filecsv:
  lista.append(x)

letras = [str(x[0]) for x in lista]
lista = list(set(letras))
lista.sort()

tabla = [(x,letras.count(x)) for x in lista]
for i,j in tabla:
    tabla = print ("{},{}".format(i,j))