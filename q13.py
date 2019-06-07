##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##


import csv
file = open('data.csv', 'r')
filecsv = csv.reader(file, delimiter= '\t')
lista = list()
for x in filecsv:
  lista.append(x)

solucion= [(i[0],i[4].split(',')) for i in lista]
solucion

for i in range(len(solucion)):
    a=0
    for j in range(len(solucion[i][1])):
        
        a += int(solucion[i][1][j][-1])
    print ("{},{}".format(solucion[i][0],a))