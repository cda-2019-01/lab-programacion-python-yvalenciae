##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##

import csv
file = open('data.csv', 'r')
filecsv = csv.reader(file, delimiter= '\t')
lista = list()
for x in filecsv:
  lista.append(x)

solucion = [(i[0],len(i[3].split(',')),len(i[4].split(','))) for i in lista]
for i,j,k in solucion:
    print ("{},{},{}".format(i,j,k))