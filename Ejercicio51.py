#Numero de empleado - Nombre - Sexo(1-mas, 2-fem) - Sueldo - Descuento - Sueldo Neto

import os

sw = True
empleados = []

while sw == True:
    os.system("clear")

    print("1. Cargar empleado nuevo")
    print("2. Ver lista de empleados")
    print("3. Obtener el resultado")
    print("4. Salir")

    opcionSeleccionada = input("Ingrese la opción deseada: ")

    if opcionSeleccionada == "4":
        sw = False

    elif opcionSeleccionada == "3":
        os.system("clear")

        if len(empleados) > 0:
            
            input("Presione Enter para continuar...")
        else:
            input("La lista de empleados esta vacía. Presione Enter para continuar...")

    elif opcionSeleccionada == "2":
        os.system("clear")

        if len(empleados) > 0:
            print(empleados)

            input("Presione Enter para continuar...")
        else:
            input("La lista de empleados esta vacía. Presione Enter para continuar...")

    elif opcionSeleccionada == "1":
        os.system("clear")

        empleado = []

        # Ingreso del numero del empleado
        numeroDeEmpleado = input("Ingrese el número del empleado: ")
        while numeroDeEmpleado.isdigit() == False:
            print("Por favor, ingrese un valor válido.")
            numeroDeEmpleado = input("Ingrese el número del empleado: ")
        
        numeroDeEmpleado = int(numeroDeEmpleado)

        # Ingreso del nombre del empleado
        nombre = input("Ingrese el nombre del empleado: ")
        
        # Ingreso del sexo del empleado
        sexo = input("Ingrese el sexo del empleado. 1 es masculino. 2 es femenino: ")

        sexoOk = False
        while sexoOk == False:
            while sexo.isdigit() == False:
                print("Por favor, ingrese un valor válido.")
                sexo = input("Ingrese el sexo del empleado. 1 es masculino. 2 es femenino: ")
            
            sexo = int(sexo)

            if sexo > 2 or sexo < 1:
                print("Por favor, ingrese un valor válido.")
                sexo = input("Ingrese el sexo del empleado. 1 es masculino. 2 es femenino: ")
            else:
                sexoOk = True
            
        # Ingreso del sueldo del empleado
        sueldo = input("Ingrese el sueldo del empleado: ")
        while sueldo.isdigit() == False:
            print("Por favor, ingrese un valor válido.")
            sueldo = input("Ingrese el sueldo del empleado: ")

        sueldo = int(sueldo)

        # Ingreso del descuento
        descuento = input("Ingrese el descuento del empleado: ")
        while descuento.isdigit() == False:
            print("Por favor, ingrese un valor válido.")
            descuento = input("Ingrese el descuento del empleado: ")

        descuento = int(descuento)

        # Calculo del Sueldo Neto
        sueldoNeto = sueldo - descuento
        print("El sueldo neto del empleado es {}".format(sueldoNeto))

        # Cargando los datos verificados en la lista empleado
        empleado.append(numeroDeEmpleado)
        empleado.append(nombre)
        empleado.append(sexo)
        empleado.append(sueldo)
        empleado.append(descuento)
        empleado.append(sueldoNeto)

        # Cargando la lista empleado en la lista empleados
        empleados.append(empleado)


        input("Presione Enter para continuar...")

    else:
        os.system("clear")
        input("Digíte una opcion válida. Presione Enter para continuar")
