##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
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
    maxmin = (l,max([x[1] for x in listagroup if x[0]==l]), min([x[1] for x in listagroup if x[0]==l]))
    print ('{},{},{}'.format(maxmin[0],maxmin[1],maxmin[2]))