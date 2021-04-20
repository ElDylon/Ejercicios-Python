frase= input("Escribir una frase\n")
cadena= input("Escribir una cadena para evaluar en la frase\n")

def evaluar_cadena(frase,cadena):
    frase = frase.lower()
    cadena = cadena.lower()
    cant = frase.count(cadena)
    return cant

print(f"la cantidad de: {cadena} en la frase es de: {evaluar_cadena(frase,cadena)}")