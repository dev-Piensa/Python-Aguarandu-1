# Suma y Promedio
# Imprimir el triangulo rectangulo inferior izquierdo
dimension = int(input("Ingrese el tamaño de la matriz: "))
matriz = []

for i in range(dimension):
    fila = []
    for j in range(dimension):
        fila.append(int(input("Ingrese un dígito: ")))
    
    matriz.append(fila)

cont = 0
for elemento in matriz:
    i = 0
    while i <= cont:
        print(elemento[i], end="")
        i = i + 1
    print("")
    cont = cont + 1