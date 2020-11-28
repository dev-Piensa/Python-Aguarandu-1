# Suma y Promedio
matriz = [[1,3,5,2,3],[3,4,7,5,8],[3,2,5,9,8],[5,4,6,3,8],[8,7,9,6,5]]
i = 0
suma = 0
promedio = 0

for elemento in matriz:
    suma = suma + elemento[i]
    i = i + 1

promedio = suma / i

print("La suma de la diagonal principal es: {}".format(suma))
print("El promedio de la diagonal principal es: {}".format(promedio))