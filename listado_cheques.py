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
            if cheque["NroCheque"] == argumentos[0]:
               print("usted busco por numero de cheque")
               print(cheque) 

    with open(path) as archivo:
          cheques = csv.DictReader(archivo)
          for cheque in cheques:
            if cheque["CodigoBanco"] == argumentos[0]:
               print("usted busco por Codigo de banco")
               print(cheque) 

    with open(path) as archivo:
          cheques = csv.DictReader(archivo)
          for cheque in cheques:
            if cheque["CodigoScursal"] == argumentos[0]:
               print("usted busco por codigo de sucursal")
               print(cheque)      
 
    with open(path) as archivo:
          cheques = csv.DictReader(archivo)
          for cheque in cheques:
            if cheque["NumeroCuentaOrigen"] == argumentos[0]:
               print("usted busco por numero de cuenta de origen")
               print(cheque)      
    with open(path) as archivo:
          cheques = csv.DictReader(archivo)
          for cheque in cheques:
            if cheque["NumeroCuentaDestino"] == argumentos[0]:
               print("usted busco por numero de cuenta de destino")
               print(cheque)  

    with open(path) as archivo:
          cheques = csv.DictReader(archivo)
          for cheque in cheques:
            if cheque["DNI"] == argumentos[0]:
               print("usted busco por numero de DNI")
               print(cheque)

    with open(path) as archivo:
          cheques = csv.DictReader(archivo)
          for cheque in cheques:
            if cheque["Estado"] == argumentos[0]:
              if cheque["DNI"] == argumentos[1]:
                DNI = cheque["DNI"]
                estado = cheque["Estado"]
                print("Usted busco los cheques con estado", estado, "del DNI:", DNI )
                print(cheque)
 

main()                

#para probar, correr en la terminal: py listado_cheques.py test.csv 11580999