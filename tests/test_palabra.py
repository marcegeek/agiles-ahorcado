from juego import Juego

# Palabra acierta
def test_palabra_acierta_mensaje():
    # Si adivina la palabra el mensaje es "ganaste".
    j = Juego('hola')
    resultado = j.arriesgarPalabra('hola')
    assert resultado == "ganaste"
    assert j.acerto

def test_palabra_acierta_progreso():
    # Si adivina la palabra el progreso esta completo.
    j = Juego('hola')
    j.arriesgarPalabra('hola')
    assert j.mostrarProgresoPalabra() == "hola"

# Palabra incorrecta
def test_palabra_incorrecta_mensaje():
    # Si arriesga palabra y es incorrecta el mensaje es "palabra incorrecta".
    j = Juego('hola')
    resultado = j.arriesgarPalabra('chau')
    assert resultado == "palabra incorrecta"

def test_palabra_incorrecta_progreso():
    # Si arriesga palabra y es incorrecta el progreso deberia mantenerse.
    j = Juego('hola')
    j.arriesgarPalabra('chau')
    assert j.mostrarProgresoPalabra() == '____'

def test_palabra_incorrecta_intentos():
    # Si arriesga palabra y los intentos disponibles deben disminuir.
    j = Juego('hola')
    j.arriesgarPalabra('chau')
    assert j.intentosDisponibles() == j.maxIntentos - j.intentosPalabra

# Palabra pierde
def test_palabra_pierde_mensaje():
    # Si arriesga palabra y se queda sin intentos el mensaje es "perdiste".
    j = Juego('hola')
    j.intentosUsados = j.maxIntentos
    resultado = j.arriesgarPalabra('chau')
    assert resultado == 'perdiste'

def test_palabra_pierde_intentos():
    # Si arriesga palabra y pierde los intentos disponibles son 0.
    j = Juego('hola')
    j.intentosUsados = j.maxIntentos
    j.arriesgarPalabra('chau')
    assert j.intentosDisponibles() == 0

# Palabra con espacios.
def test_palabra_con_espacios_progreso():
    j = Juego("hola mundo")
    j.arriesgarLetra('o')
    assert j.mostrarProgresoPalabra() == '_o__ ____o'