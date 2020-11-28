import os
# El indice 0 equivale al Número de Alumno
# El indice 1 equivale al Nombre
# El indice 3 equivale al puntaje de Aritmética y Álgebra
# El indice 4 equivale al puntaje de Geometría y Trigonometría
# El indice 5 equivale al puntaje de Castellano
# El indice 6 equivale al puntaje de Test de Aptitud

sw = True
alumnos = []

while sw == True:
    os.system("clear")
    print("1. Cargar alumno nuevo")
    print("2. Ver lista de alumnos")
    print("3. Obtener el resultado")
    print("4. Salir")
  
    opcionSeleccionada = input("Ingrese la opción deseada: ")

    if opcionSeleccionada == "4":
        sw = False
    elif opcionSeleccionada == "3":
        os.system("clear")

        if len(alumnos) > 0:
            # print("A) ----PROMEDIO DE PUNTAJE POR CADA ALUMNO----")
            for i in alumnos:
                prom = 0
                for j in range(2,6):
                    prom = prom + i[j]
                
                prom = prom / 4
                
                print("El promedio de puntaje de {} es {}".format(i[1], prom))
            print("")
            # print("B) ----PROMEDIO GENERAL DE CASTELLANO----")

            prom = 0
            cont = 0
            for i in alumnos:
                prom = prom + i[4]
                cont = cont + 1
            
            prom = prom / cont

            print("El promedio general de Castellano es {}".format(prom))
            print("")


            maximoPuntaje = False
            for i in alumnos:
                if i[5] == 100:
                    maximoPuntaje = True
            
            if maximoPuntaje == True:
                print("HUBO MAXIMO PUNTAJE")
                print("")

            menorPuntaje = alumnos[0][3]
            for i in alumnos:
                if i[3] <= menorPuntaje:
                    menorPuntaje = i[3]
                    alumnoMenorPuntaje = i
            
            
            print("{} obtuvo el menor puntaje en trigonometría".format(alumnoMenorPuntaje[1]))
            print("")

            input("Presione Enter para continuar...")
        else:
            input("La lista de alumnos esta vacía. Presione Enter para continuar...")

    elif opcionSeleccionada == "2":
        os.system("clear")

        if len(alumnos) > 0:
            print(alumnos)
            input("Presione Enter para continuar...")
        else:
            input("La lista de alumnos esta vacía. Presione Enter para continuar...")

    elif opcionSeleccionada == "1":
        os.system("clear")

        alumno = []

        #Ingreso del numero del alumno
        numeroDeAlumno = input("Ingrese el número de alumno: ")
        while numeroDeAlumno.isdigit() == False:
            print("Por favor, ingrese un valor válido.")
            numeroDeAlumno = input("Ingrese el número de alumno: ")
        
        numeroDeAlumno = int(numeroDeAlumno)

        #Ingreso del nombre del alumno
        nombre = input("Ingrese el nombre del alumno: ")

        #Ingreso del puntaje de Aritmética y Álgebra del alumno
        aritmeticaAlgebra = input("Ingrese el puntaje de Aritmética y Álgebra: ")
        while aritmeticaAlgebra.isdigit() == False:
            print("Por favor, ingrese un valor válido.")
            aritmeticaAlgebra = input("Ingrese el puntaje de Aritmética y Álgebra: ")
        
        aritmeticaAlgebra = int(aritmeticaAlgebra)

        #Ingreso del puntaje de Geometría y Trigonometría del alumno
        geometriaTrigonometria = input("Ingrese el puntaje de Geometría y Trigonometría: ")
        while geometriaTrigonometria.isdigit() == False:
            print("Por favor, ingrese un valor válido.")
            geometriaTrigonometria = input("Ingrese el puntaje de Geometría y Trigonometría: ")
        
        geometriaTrigonometria = int(geometriaTrigonometria)

        #Ingreso del puntaje de Castellano del alumno
        castellano = input("Ingrese el puntaje de Castellano: ")
        while castellano.isdigit() == False:
            print("Por favor, ingrese un valor válido.")
            castellano = input("Ingrese el puntaje de Castellano: ")
        
        castellano = int(castellano)

        #Ingreso del puntaje del Test de Aptitud del alumno
        testAptitud = input("Ingrese el puntaje del Test de Aptitud: ")
        while testAptitud.isdigit() == False:
            print("Por favor, ingrese un valor válido.")
            testAptitud = input("Ingrese el puntaje del Test de Aptitud: ")
        
        testAptitud = int(testAptitud)

        #Cargando los datos verificados en la lista alumno
        alumno.append(numeroDeAlumno)
        alumno.append(nombre)
        alumno.append(aritmeticaAlgebra)
        alumno.append(geometriaTrigonometria)
        alumno.append(castellano)
        alumno.append(testAptitud)

        #Cargando la lista alumno en la lista alumnos
        alumnos.append(alumno)

    else:
        os.system("clear")
        input("Digíte una opcion válida. Presione Enter para continuar...")

os.system("clear")