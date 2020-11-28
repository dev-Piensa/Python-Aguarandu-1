#Numero de empleado - Nombre - sexo(1-fem 2-mas) - Sueldo - Cantidad de hijos

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
            # Listar numero de empleado - nombre - sueldo de los hombres con sueldos menor o igual a 40.000G
            for i in empleados:
                if i[2] == 2 and i[3] <= 40000:
                    print("{} - {} - {}".format(i[0], i[1], i[3]))

            # Listar numero de empleado - nombre - sueldo - cantidad de hijos de las mujeres
            # con sueldo mayor a 70.000G y con mas de 2 hijos
            for i in empleados:
                if i[1] == 1 and i[3] > 70000 and i[4] > 2:
                    print("{} - {} - {} - {}".format(i[0], i[1], i[3], i[4]))

            # Buscar e imprimir el nombre y sueldo del empleado con sueldo mayor y contar e imprimir la cantidad de hombres y mujeres
            # empleadas en la empresa.
            mayorSueldo = empleados[0][3]
            for i in empleados:
                if mayorSueldo <= i[3]:
                    mayorSueldo = i[3]
                    empleadoMayorSueldo = i
            
            print("El sueldo de {} es de {}".format(empleadoMayorSueldo[1], empleadoMayorSueldo[3]))
            print("")

            contHombres = 0
            contMujeres = 0
            for i in empleados:
                if i[2] == 2:
                    contHombres = contHombres + 1
                elif i [2] == 1:
                    contMujeres = contMujeres + 1

            print("La cantidad de hombres empleados en la empresa es {}".format(contHombres))
            print("La cantidad de mujeres empleadas en la empresa es {}".format(contMujeres))

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

        #Ingreso del numero del empleado
        numeroDeEmpleado = input("Ingrese el número de empleado: ")
        while numeroDeEmpleado.isdigit() == False:
            print("Por favor, ingrese un valor válido.")
            numeroDeEmpleado = input("Ingrese el número de empleado: ")
        
        numeroDeEmpleado = int(numeroDeEmpleado)

        #Ingreso del nombre del empleado
        nombre = input("Ingrese el nombre del empleado: ")

        #Ingreso del sexo del empleado
        sexo = input("Ingrese el sexo del empleado. 1 es femenino. 2 es masculino: ")

        sexoOk = False
        while sexoOk == False:
            while sexo.isdigit() == False:
                print("Por favor, ingrese un valor válido.")
                sexo = input("Ingrese el sexo del empleado. 1 es femenino. 2 es masculino: ")

            sexo = int(sexo)

            if sexo > 2 or sexo < 1:
                print("Por favor, ingrese un valor válido.")
                sexo = input("Ingrese el sexo del empleado. 1 es femenino. 2 es masculino: ")
            else:
                sexoOk = True

        # Ingreso del sueldo del empleado
        sueldo = input("Ingrese el sueldo del empleado: ")
        while sueldo.isdigit() == False:
            print("Por favor, ingrese un valor válido.")
            sueldo = input("Ingrese el sueldo del empleado: ")
        
        sueldo = int(sueldo)

        # Ingreso de la cantidad de hijos del empleado
        hijos = input("Ingrese la cantidad de hijos del empleado: ")
        while hijos.isdigit() == False:
            print("Por favor, ingrese un valor válido.")
            hijos = input("Ingrese la cantidad de hijos del empleado: ")
        
        hijos = int(hijos)

        # Cargando los datos verificados en la lista empleado
        empleado.append(numeroDeEmpleado)
        empleado.append(nombre)
        empleado.append(sexo)
        empleado.append(sueldo)
        empleado.append(hijos)

        # Cargando la lista empleado en la lista empleados
        empleados.append(empleado)

        input("Presione Enter para continuar...")
    else:
        os.system("clear")
        input("Digíte una opcion válida. Presione Enter para continuar")

os.system("clear")