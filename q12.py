##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##


import csv
file = open('data.csv', 'r')
filecsv = csv.reader(file, delimiter= '\t')
lista = list()
for x in filecsv:
  lista.append(x)

tabla = []
solo_letra = []
for l in lista:  
    t = [(int(l[1]),letra) for letra in l[3].split(',')]
    sl = [letra for letra in l[3].split(',')]
    tabla += t
    solo_letra += sl

solo_letra_uni = list(set(solo_letra))
solo_letra_uni.sort()


for l in solo_letra_uni:
    a=0
    for i,j in tabla:
        if l == j:
            a += i
    print ("{},{}".format(l,a))