cadena = input("Ingresa la clave(debe tener menos de 10 caracteres y no\
contener los simbolos: @ y !):\n")

if len(cadena)> 10:
    print("Ingresaste mas de 10 caracteres")
cant= cadena.count("@") + cadena.count("!")
if cant >= 1:
    print("Ingresaste alguno de estos símbolos: @ o !")
else:
    print("Ingreso OK")