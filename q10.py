##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
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

solucion = [(x,solo_letras.count(x)) for x in letras_unicas]

for tabla in solucion:
    print ("{},{}".format(tabla[0],tabla[1]))
