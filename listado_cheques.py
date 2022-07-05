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
                    print(f'Numero de cheque: {cheque["NroCheque"]}\nCodigo del banco {cheque["CodigoBanco"]}\nCodigo de sucursal: {cheque["CodigoScurusal"]}\nNumero de Cuenta de Origen: {cheque["NumeroCuentaOrigen"]}\nNumero de Cuenta de Destino: {cheque["NumeroCuentaDestino"]}\nValor Total: {cheque["Valor"]}\nFecha de Origen: {cheque["FechaOrigen"]}\nFecha de Pago: {cheque["FechaPago"]}\nDNI: {cheque["DNI"]}\nTipo: {cheque["Tipo"]}\nEstado: {cheque["Estado"]}\n')   
print("***********************")
print("Lista de Cheques")
print("")
main()
print("***********************")                

#para probar, correr en la terminal: py listado_cheques.py test.csv 11580999