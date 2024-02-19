
def gestion_de_trainer(occion):
    if occion==1:
        registrar_trainer()

import json

def registrar_trainer():
    documento = input("Ingrese su documento: ")
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    telefono = input("Ingrese su teléfono: ")
    fijo = input("Ingrese el número de teléfono fijo: ")

    trainer = {"doc": documento, "nombre": nombre, "edad": edad, "telefono": telefono, "fijo": fijo,"estado":"rechasado"}

    
    with open('registrartrainer.json', 'r') as file:
        # Cargar datos existentes desde el archivo si hay alguno
        trainers = json.load(file)


    trainers.append(trainer)

    with open('registrartrainer.json', 'w') as file:
        # Guardar la lista actualizada en el archivo JSON
        json.dump(trainers, file, indent=2)

    print("*****************************")
    print("******* Trainer guardado *******")
    print("*****************************")



