def hola_mundo():
    mensaje = "Hola, Mundo"
    print(mensaje)
    with open("mensaje.txt", "w") as archivo:
        archivo.write(mensaje)

# Llamar a la función
hola_mundo()

def suma(a, b):
    return a + b

print("La suma de 5 + 3 es:", suma(5, 3))
