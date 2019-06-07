##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##


import csv
file = open('data.csv', 'r')
filecsv = csv.reader(file, delimiter= '\t')
lista = list()
for x in filecsv:
  lista.append(x)

numeros = [(x[1]) for x in lista]
letras = [str(x[0]) for x in lista]
entrada = [(x[1],str(x[0])) for x in lista]

Numero_unicos = list(set(numeros))
Numero_unicos.sort()

solucion = [(x, [y for z,y in entrada if x==z]) for x in Numero_unicos]
solucion = [(x, sorted(y)) for x,y in solucion]


for x in solucion:
  print (x)