import csv
import sys
from datetime import datetime
import time

# Por si se especifica estado
if len(sys.argv) == 7:
    RUTA_ARCHIVO = sys.argv[1]
    DNI = sys.argv[2]
    SALIDA = sys.argv[3]  
    TIPO = sys.argv[4]
    ESTADO = sys.argv[5]
    F_INICIO, F_FIN = sys.argv[6].split(':')
    
# Por si no se especifica estado
if len(sys.argv) == 6:
    RUTA_ARCHIVO = sys.argv[1]
    DNI = sys.argv[2]
    SALIDA = sys.argv[3]  
    TIPO = sys.argv[4]
    ESTADO = None
    F_INICIO, F_FIN = sys.argv[5].split(':')


with open(RUTA_ARCHIVO) as f:
    cheques = csv.DictReader(f)

    porDNI = list(filter(lambda cheque: cheque['DNI'] == DNI , cheques))

    porTipo = list(filter(lambda cheque: cheque['Tipo'] == TIPO , porDNI))

    if ESTADO:
        # Lo guardo en porTipo para no tener que crear una variable que en algunas ocasiones no existe
        porTipo = list(filter(lambda cheque: cheque['Estado'] == ESTADO , porTipo))

    F_INICIO = datetime.strptime(F_INICIO, "%d-%m-%Y").timestamp()
    F_FIN = datetime.strptime(F_FIN, "%d-%m-%Y").timestamp()

    porFecha = list(filter(lambda cheque: F_INICIO < int(cheque['FechaOrigen']) < F_FIN, porTipo))
    
    if SALIDA == "PANTALLA":
        print(porFecha)

    if SALIDA == "CSV":
        ahora = datetime.now().strftime('%d%m%y%y')
        with open(f'{DNI}-{ahora}.csv', 'w') as f:
            if porFecha:
                f.write(', '.join(porFecha[0].keys()))
                f.write('\n')

            for cheque in porFecha:
                f.write(', '.join(cheque.values()))
                f.write('\n')


# Para tests     
# py main.py test.csv 11580999 CSV EMITIDO APROBADO 01-01-1990:10-10-2090
