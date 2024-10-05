import random

def cargar_palabras(ruta):
    '''
    Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
    dichas palabras en una lista.
    '''
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        return res
    
def elegir_palabra(palabras):
    palabra = random.choice(palabras)
    return palabra


def enmascarar_palabra(palabra,letras_probadas):
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la lista 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena concatenando los elementos de la lista (ver 'Ayuda')
    Ayuda: 
    - Utilice el método join de las cadenas. Observe el siguiente ejemplo:
        ' '.join(['a','b','c']) # Devuelve "a b c"
    '''
    palabra_juego = []
    for letra in palabra:
        if letra in letras_probadas:
            palabra_juego.append(letra)
        else:
            palabra_juego.append("_")
    return ' '.join(palabra_juego)

def pedir_letra(letras_probadas):
    '''
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada ya se había propuesto antes y pedir otra si es así
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    ''' 
    letra_elegida = input("escriba la siguiente letra:").lower()
    while letra_elegida in letras_probadas:
        letra_elegida = input("Ya has probado esa letra, ponga otra:").lower()
    return letra_elegida

def comprobar_letra(palabra_secreta, letra):
    '''
    Comprobar letra:
    - Comprobar si la letra está en la palabra secreta o no
    - Mostrar el mensaje correspondiente informando al usuario
    - Devolver True si estaba y False si no
    '''
    
    acierto = letra in palabra_secreta
    if acierto :
          print("Letra correcta")       
    else:
          print("Has fallado, vuelve a intentarlo")
    return acierto

def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    '''
    Comprobar si se ha completado la palabra:
    - Comprobar si todas las letras de la palabra secreta han sido propuestas por el usuario
    - Devolver True si es así o False si falta alguna letra por adivinar
    '''
    for letra in palabra_secreta:
        if letra not in letras_probadas:
            return False
    return True 

def ejecutar_turno(palabra_secreta, letras_probadas):
    '''
    Ejecutar un turno de juego:
    - Mostrar la palabra enmascarada
    - Pedir la nueva letra
    - Comprobar si la letra está en la palabra (acierto) o no (fallo)
    - Añadir la letra al conjunto de letras probadas
    - Devolver True si la letra fue un acierto, False si fue un fallo
    Ayuda:
    - Recuerda las funciones que ya has implementado para mostrar la palabra, pedir la letra y comprobarla
    '''
    print(palabra_secreta)
    letra_elegida = input("escriba la siguiente letra:").lower()
    while letra_elegida in letras_probadas:
        letra_elegida = input("Ya has probado esa letra, ponga otra:").lower()
    letras_probadas.add(letra_elegida)
    for letra in palabra_secreta:
        if letra not in letras_probadas:
            return False
        else:
            return True


def eleccion_modo():
    modo_juego = input("¿ A que quieres jugar?, elegir palabra o palabra aleatoria:")
    while modo_juego not in ["elegir palabra", "palabra aleatoria"]:

       modo_juego = input("porfavor elija: elegir palabra o palabra aleatoria:" )
    return modo_juego

def elegir_palabra_jugador():
    palabra = input("que palabra elijes:")
    return palabra


if __name__ == "__main__":
    modo_juego = eleccion_modo()
    if modo_juego == "palabra aleatoria":
        palabras = cargar_palabras("ahorcado/LAB-Ahorcado-main\data\palabras_ahorcado.txt")
        palabra_elegida = elegir_palabra(palabras)
    elif modo_juego == "elegir palabra":
        palabra_elegida = elegir_palabra_jugador()
    print(palabra_elegida)
    enmascarar_palabra(palabra_elegida,letras_probadas)


