frase= """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar 
un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir 
alguna pequeña base de datos personalizada, o una aplicación especializada con 
interfaz gráfica, o UN juego simple.
"""
def obtener_lista(frase):
    lista = frase.lower().replace('.','').split()
    print(lista)
    return lista

def lista_sin_duplicados(lista):
    nueva_lista= list(dict.fromkeys(lista))
    print(nueva_lista)

lista_sin_duplicados(obtener_lista(frase))