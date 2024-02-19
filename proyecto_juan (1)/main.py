import menus


while(True):
    try:
        opcion = menus.menu_principal()
        if opcion == 1:
            menus.menu_del_camper()
        elif opcion == 2:
            menus.menu_del_tariner()
        elif opcion == 3:
            menus.menu_del_cordinador()
        elif opcion == 0:
            if(menus.confirmacion() == True):
                break
        else:
            print("********************************")
            print("El valor no está en las opciones")
            print("********************************")
    except Exception as e:
        print(e)
        print("**************************")
        print("Ingrese una opción válida")
        print("**************************")

