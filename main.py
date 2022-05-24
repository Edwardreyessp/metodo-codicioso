from asyncio.windows_events import INFINITE
from os import lstat


def Codicioso():
    trabajoEscogido = []
    valor = int(INFINITE)
    escogido = 0
    for i in range (0, filas):
        for j in range (0, columnas):
            if int(Personas[i].trabajos[j]) < valor and not (j in trabajoEscogido):
                escogido = j
                valor = int(Personas[i].trabajos[j])
        valor = int(INFINITE)
        trabajoEscogido.append(escogido)
        Personas[i].trabajo = "P" + str(i + 1) + "T" + str(escogido + 1)
    #archivo = open("salidaP3_2.txt", "w")
    salida.write("F1\n")
    for i in Personas:
        salida.write(i.trabajo + " ")


def CodiciosoPorColumnas():
    columnaGlobal = []
    personaEscogida = []
    orden = []
    suma = 0
    valor = int(INFINITE)
    for i in range(0, filas):
        for j in range(0, columnas):
            suma += int(Personas[j].trabajos[i])
        columnaGlobal.append((i, suma))
        suma = 0
    
    for i in range(0, len(columnaGlobal)):
        for j in range(0, len(columnaGlobal) - i - 1):
            if columnaGlobal[j][1] < columnaGlobal[j + 1][1]:
                columnaGlobal[j], columnaGlobal[j + 1] = columnaGlobal[j + 1], columnaGlobal[j]

    for i in columnaGlobal:
        orden.append(i[0])

    for i in orden:
        for j in range (0, filas):
            if int(Personas[j].trabajos[i]) < int(valor) and not (j in personaEscogida):
                escogido = j
                valor = Personas[j].trabajos[i]
                Personas[j].trabajo = "P" + str(j + 1) + "T" + str(i + 1)
        valor = int(INFINITE)
        personaEscogida.append(escogido)

    salida.write("\n\nF3.1\n")
    for i in Personas:
        salida.write(i.trabajo + " ")


def CodiciosoPorFilas():
    filaGlobal = []
    filaEscogida = []
    orden = []
    suma = 0
    valor = int(INFINITE)
    repetido = 0
    lista = []
    filaActual = 0
    flag = 0
    
    for i in range(0, filas):
        for j in range(0, columnas):
            suma += int(Personas[i].trabajos[j])
        filaGlobal.append((i, suma))
        suma = 0
    
    for i in range(0, len(filaGlobal)):
        for j in range(0, len(filaGlobal) - i - 1):
            if filaGlobal[j][1] < filaGlobal[j + 1][1]:
                filaGlobal[j], filaGlobal[j + 1] = filaGlobal[j + 1], filaGlobal[j]


    for i in filaGlobal:
        orden.append(i[0])
    
    lista2 = []

    for i in orden:
        for j in range(0, columnas):
            if int(Personas[i].trabajos[j]) < int(valor) and not (j in filaEscogida):
                escogido = j
                valor = Personas[i].trabajos[j]
                Personas[i].trabajo = "P" + str(i + 1) + "T" + str(j + 1)
        for k in range (0, columnas):
            if int(Personas[i].trabajos[k]) == int(valor):
                flag += 1
                if flag > 1:
                    lista = [i, k]
        filaActual += 1
        flag = 0
        valor = int(INFINITE)
        filaEscogida.append(escogido)

    filaActual = 0

    salida.write("\n\nF3\n")
    for i in Personas:
        salida.write(i.trabajo + " ")

    valor = int(INFINITE)
    filaEscogida = []
    lista2 = [4, 0]

    for i in orden:
        for j in range(0, columnas):
            if int(Personas[i].trabajos[j]) <= int(valor):
                if i == lista[0] and j == lista[1]:
                    valor = Personas[i].trabajos[j]
                    escogido = j
                    Personas[i].trabajo = "P" + str(i + 1) + "T" + str(lista[1] + 1)
                    Personas[orden[filaActual + 1]].trabajo = "P" + str(orden[filaActual + 1] + 1) + "T" + str(lista2[1] + 1)
        filaActual += 1
        valor = int(INFINITE)
        filaEscogida.append(escogido)

    salida.write("\n")
    for i in Personas:
        salida.write(i.trabajo + " ")


def CodiciosoDoble():
    orden = []
    orden2 = []
    personaEscogida = []
    valor = 0
    valor2 = 0
    for i in range(0, filas):
        for j in range(0, filas):
            for k in range(0, columnas):
                if int(Personas[j].trabajos[k]) > valor and not k in orden:
                    valor = int(Personas[j].trabajos[k])
                    valor2 = k
        orden.append(valor2)
        valor = 0

    valor = int(INFINITE)

    for i in orden:
        for j in range (0, filas):
            if int(Personas[j].trabajos[i]) < int(valor) and not (j in personaEscogida):
                escogido = j
                valor = Personas[j].trabajos[i]
                Personas[j].trabajo = "P" + str(j + 1) + "T" + str(i + 1)
        valor = int(INFINITE)
        personaEscogida.append(escogido)

    salida.write("\n\nF2\n")
    for i in Personas:
        salida.write(i.trabajo + " ")

class Persona:
    trabajos = []
    trabajo = ""

archivo = open("datosP3_2.txt", "r")
#print(archivo.read())

Personas = []
filas = 0
columnas = 0

for line in archivo:
    Personas.append(Persona())
    trabajos = []
    columnas = 0
    for number in line.split():
        trabajos.append(number)
        columnas += 1
    Personas[filas].trabajos = trabajos
    filas += 1

salida = open("salidaP3_2.txt", "w")

# Codicioso por filas F1
Codicioso()

# Codicioso por columnas global F2
CodiciosoDoble()

# Criterio por sumatoria de filas F3
CodiciosoPorFilas()

# Codicioso precio más alto por columnas F3.1
CodiciosoPorColumnas()