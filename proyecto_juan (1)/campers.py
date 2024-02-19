
def gestion_de_campers(opc):
    if opc==1:
        registrar_camper()
    else:
        print("***********************************")
        print("*ese valor no esta en las opciones*")
        print("***********************************")



import json

def registrar_camper():
    documento = input("Ingrese su documento :")
    nombre = input("Ingrese su nombre :")
    edad = input("Ingrese su edad :")
    telefono = input("ingrese su telefono :")
    fijo = input("ingrese el numero de telefono fijo :")
    
    camper = {"doc": documento, "nombre": nombre, "edad": edad,"telefono":telefono,"fijo":fijo,"estado":"aseptado"}

    with open('registrarcamper.json', 'r') as file:
        # Cargar datos existentes desde el archivo si hay alguno
        campers = json.load(file)

        
    campers.append(camper)

    with open('registrarcamper.json', 'w') as file:
        # Guardar la lista actualizada en el archivo JSON
        json.dump(campers, file, indent=2)

    print("*****************************")
    print("******* Camper guardado *******")
    print("*****************************")

