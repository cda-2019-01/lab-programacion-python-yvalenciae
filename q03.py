##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##

import csv
file = open('data.csv', 'r')
filecsv = csv.reader(file, delimiter= '\t')
lista = list()
for x in filecsv:
  lista.append(x)

letras = [str(x[0]) for x in lista]
listaletras = list(set(letras))
listaletras.sort()


listagroup = [(lista[x][0], int(lista[x][1])) for x in range(len(lista))]

for l in listaletras:
    suma = (l,sum([x[1] for x in listagroup if x[0]==l]))
    print ('{},{}'.format(suma[0],suma[1]))