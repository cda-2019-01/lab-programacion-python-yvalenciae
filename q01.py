##
## Imprima la suma de la segunda columna.
##
import csv
file = open('data.csv', 'r')
filecsv = csv.reader(file, delimiter= '\t')
lista = list()
for x in filecsv:
  lista.append(x)

col2 = [int(x[1]) for x in lista]
print(sum(col2))