import string
texto = '''La falsedad de un juicio no es para nosotros ya una objeción contra él; acaso sea en esto en lo que más extraño suene nuestro nuevo lenguaje.
La cuestión está en saber hasta qué punto ese juicio favorece la vida,
conserva la vida, conserva la especie, quizá incluso selecciona la especie; y nosotros estarnos inclinados
por principio a afirmar que los juicios más falsos (de ellos forman parte los juicios sintéticos a priori) son
los más imprescindibles para nosotros, que el hombre no podría vivir si no admitiese las ficciones lógicas,
si no midiese la realidad con el metro del mundo puramente inventado de lo incondicionado, idéntico-a-símismo,
 si no falsease permanentemente el mundo mediante el número, - que renunciar a los juicios falsos
sería renunciar a la vida, negar la vida. Admitir que la no-verdad es condición de la vida: esto significa,
desde luego, enfrentarse de modo peligroso a los sentimientos de valor habituales; y una filosofía que osa
hacer esto se coloca, ya sólo con ello, más allá del bien y del mal. '''
print(texto)

def contar_letras (texto):
    ''' Se cuentan las letras iniciales al principio de que cada palabra en el texto y se retorna el resultado'''
    lista = texto.split()
    print(lista)
    cont = 0
    letra= input('\nIngrese una letra para evaluar en el texto\n')
    if string.ascii_letters.find(letra) != -1:
      for palabra in lista:
          if palabra.lower().startswith(letra):
              cont = cont + 1
      print(f'la letra: {letra}, aparece {cont} veces en el texto')
    else:
        print('\nNo se ingreso una letra')

contar_letras(texto)
