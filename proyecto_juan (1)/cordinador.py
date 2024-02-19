import json



def gestion_del_coordinador(opc):
    if opc==1:
        cambiar_estado_del_camper()
    if opc==2:
        cambiar_estado_del_camper2()
    if opc==3:
        admitir_nuevo_trainer()
    if opc==4:
        rechasar_trainer()

    else:
        print("***********************************")
        print("*ese valor no esta en las opciones*")
        print("***********************************")



def cambiar_estado_del_camper():
    documento = input("Ingrese su documento :")
    nombre = input("Ingrese su nombre :")
    edad = input("Ingrese su edad :")
    telefono = input("ingrese su telefono :")
    fijo = input("ingrese el numero de telefono fijo :")
    ruta_de_entrenamiento=input("porfavor asigne la ruta de entrenamiento")
    area_de_entrenamiento=input("porfeavor asigne un are de entrenamiento las areas de entrenamiento son apolo artemis y spuknik :")
    nota_del_examen=input("ingrese la nota del examen")
    asignar_trainer=input("asigne un trainer")
    horario=input("ingrese si el horario del camper es en la mañana o en la tarde")
    camper = {"doc": documento, "nombre": nombre, "edad": edad,"telefono":telefono,"fijo":fijo,"estado":"aseptado","ruta":ruta_de_entrenamiento,"area":area_de_entrenamiento,"nota":nota_del_examen,"trainer":asignar_trainer,"horario":horario}

    with open('campers_aceptados.json', 'r') as file:
    
        campers = json.load(file)

        
    campers.append(camper)

    with open('campers_aceptados.json', 'w') as file:
        # Guardar la lista actualizada en el archivo JSON
        json.dump(campers, file, indent=2)

    print("*******************************")
    print("******* Camper guardado *******")
    print("*******************************")
    

def cambiar_estado_del_camper2():
    documento = input("Ingrese su documento :")
    nombre = input("Ingrese su nombre :")
    edad = input("Ingrese su edad :")
    telefono = input("ingrese su telefono :")
    fijo = input("ingrese el numero de telefono fijo :")
   
    camper = {"doc": documento, "nombre": nombre, "edad": edad,"telefono":telefono,"fijo":fijo,"estado":"rechasado"}

    with open('campers_rechasados.json', 'r') as file:
        
        campers = json.load(file)

        
    campers.append(camper)

    with open('campers_rechasados.json', 'w') as file:
        # Guardar la lista actualizada en el archivo JSON
        json.dump(campers, file, indent=2)

    print("*******************************")
    print("******* Camper rechasado ******")
    print("*******************************")
    
def admitir_nuevo_trainer():
    documento = input("Ingrese su documento :")
    nombre = input("Ingrese su nombre :")
    edad = input("Ingrese su edad :")
    telefono = input("ingrese su telefono :")
    fijo = input("ingrese el numero de telefono fijo :")
    
    trainer2 = {"doc": documento, "nombre": nombre, "edad": edad,"telefono":telefono,"fijo":fijo,"estado":"aseptado"}

    with open('trainer_aceptado.json', 'r') as file:
       
        trainers2 = json.load(file)

        
    trainers2.append(trainer2)

    with open('trainer_aceptado.json', 'w') as file:
        # Guardar la lista actualizada en el archivo JSON
        json.dump(trainers2, file, indent=2)

    print("*******************************")
    print("******* Camper guardado *******")
    print("*******************************")
    

def rechasar_trainer():
    documento = input("Ingrese su documento :")
    nombre = input("Ingrese su nombre :")
    edad = input("Ingrese su edad :")
    telefono = input("ingrese su telefono :")
    fijo = input("ingrese el numero de telefono fijo :")
    
    trainer = {"doc": documento, "nombre": nombre, "edad": edad,"telefono":telefono,"fijo":fijo,"estado":"aseptado"}

    with open('trainer_rechasado.json', 'r') as file:
       
        trainers = json.load(file)

        
    trainers.append(trainer)

    with open('trainer_rechasado.json', 'w') as file:
        # Guardar la lista actualizada en el archivo JSON
        json.dump(trainers, file, indent=2)

    print("*******************************")
    print("******* Camper rechasado ******")
    print("*******************************")