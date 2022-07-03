import csv
import sys
import os

def main():
     
     PATH_TEST = sys.argv[1]
     args = sys.argv[2:]
     
     leerCsv(PATH_TEST, args)
     
     
def leerCsv(path, argumentos):
     
    with open(path) as archivo:
          cheques = csv.DictReader(archivo)
          for cheque in cheques:
            if cheque["DNI"] == argumentos[0]:
                 print(cheque)      
 
main()                

#para probar, correr en la terminal: py listado_cheques.py test.csv 11580999