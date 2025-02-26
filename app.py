def hola_mundo():
    mensaje = "Hola, Mundo"
    print(mensaje)
    with open("mensaje.txt", "w") as archivo:
        archivo.write(mensaje)

# Llamar a la función
hola_mundo()
