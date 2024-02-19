import campers
import trainer
import cordinador
def menu_principal():
    print("""____bien venido al menu principal____
        1.menu del camper
        2.menu del trainer
        3.menu del cordinador
        0.salir
        """)
    opcion =  int(input("ingrese la occion deseada :"))
    return opcion

def menu_del_camper():
    print("""____bienvenido a las occiones del camper____
        1.registrarse
        0.salir al menu principal
        """)
    opc = int(input("ingrese la opcion deseada :"))
    campers.gestion_de_campers(opc)

def menu_del_tariner():
    print("""____bienvenido al menu del tarainer____
        1.registrarse 
        0.salir al menu principal
        """)
    opc= int(input("ingrese la opcion deseada :"))
    trainer.gestion_de_trainer(opc)

def menu_del_cordinador():
    print("""____bienvenido al menu del coordinador____
        1.cambiar estado del camper a aseptado
        2.cambiar estado del camper a rechasado
        3.cambiar estado del trainer a aseptado
        4.cambiar estado del trainer a rechasado
        
        0.salir al menu principaf
        """)
    opc = int(input("ingrese la opcion deseada :"))
    cordinador.gestion_del_coordinador(opc)

def confirmacion():
    validacion = input("Ingrese salir para salir o cualquier otra opción o valor para continuar :")
    if(validacion.lower() == "salir"):
        return True
    else:
        return False
    
