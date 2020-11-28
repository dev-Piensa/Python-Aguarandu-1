palabra = input("Ingrese una palabra: ")
palabraInvertida = ""

for i in range(len(palabra)-1, -1, -1):
    palabraInvertida = palabraInvertida + palabra[i]

print(palabra)
print(palabraInvertida)