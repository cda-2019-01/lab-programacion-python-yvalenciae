##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##

import csv
file = open('data.csv', 'r')
filecsv = csv.reader(file, delimiter= '\t')
lista = list()
for x in filecsv:
  lista.append(x)

fechas = [x[2] for x in lista]
meses = [date[5:7] for date in fechas]
mes = list(set(meses))
mes.sort()
mes


solucion = [(m ,meses.count(m)) for m in mes]
for i,j in solucion:
    print ("{},{}".format(i,j))