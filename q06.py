##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##

import csv
file = open('data.csv', 'r')
filecsv = csv.reader(file, delimiter= '\t')
lista = list()
for x in filecsv:
  lista.append(x)

cadena = [x[4].split(',') for x in lista]

listascad = [c for lista in cadena for c in lista]
tabla= [(dato.split(':')) for dato in listascad]
solo_letras = [l[0:3] for l in listascad]
letras_unicas = list(set (solo_letras))
letras_unicas.sort()
letras_unicas

listagroup = [(tabla[x][0], int(tabla[x][1])) for x in range(len(tabla))]

for l in letras_unicas:
    maxmin = (l,min([x[1] for x in tabla if x[0]==l]), max([x[1] for x in tabla if x[0]==l]))
    print ('{},{},{}'.format(maxmin[0],maxmin[1],maxmin[2]))