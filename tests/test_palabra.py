from juego import Juego

# Palabra acierta
def test_palabra_acierta_mensaje():
    # Si adivina la palabra el mensaje es "palabra correcta" y acerto=True.
    j = Juego('hola')
    resultado = j.arriesgarPalabra('hola')
    assert resultado == "palabra correcta"
    assert j.acerto

def test_palabra_acierta_finalizo():
    j = Juego('hola')
    j.arriesgarPalabra('hola')
    assert j.finalizo()

def test_palabra_acierta_progreso():
    # Si adivina la palabra el progreso esta completo.
    j = Juego('hola')
    j.arriesgarPalabra('hola')
    assert j.finalizo() and j.mostrarProgresoPalabra() == "hola"

def test_palabra_acierta_sin_errores_puntaje():
    j = Juego('hola')
    j.arriesgarPalabra('hola')
    assert j.finalizo() and j.puntaje() == j.maxIntentos

def test_palabra_acierta_un_error_puntaje():
    j = Juego('hola')
    # pierde dos intentos
    j.arriesgarPalabra('hoja')
    j.arriesgarPalabra('hola')
    assert j.finalizo() and j.puntaje() == j.maxIntentos - 2

def test_palabra_acierta_dos_errores_puntaje():
    j = Juego('hola')
    # pierde cuatro intentos
    j.arriesgarPalabra('hoja')
    j.arriesgarPalabra('loza')
    j.arriesgarPalabra('hola')
    assert j.finalizo() and j.puntaje() == j.maxIntentos - 4

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
def test_palabra_pierde_perdio():
    j = Juego('hola')
    j.intentosUsados = j.maxIntentos
    resultado = j.arriesgarPalabra('chau')
    assert j.perdio()

def test_palabra_pierde_finalizo():
    j = Juego('hola')
    j.intentosUsados = j.maxIntentos
    resultado = j.arriesgarPalabra('chau')
    assert j.finalizo()

def test_palabra_pierde_mensaje():
    # Si arriesga palabra y se queda sin intentos el mensaje es "palabra incorrecta".
    j = Juego('hola')
    j.intentosUsados = j.maxIntentos
    resultado = j.arriesgarPalabra('chau')
    assert resultado == 'palabra incorrecta'

def test_palabra_pierde_intentos():
    # Si arriesga palabra y pierde los intentos disponibles son 0.
    j = Juego('hola')
    j.intentosUsados = j.maxIntentos
    j.arriesgarPalabra('chau')
    assert j.intentosDisponibles() == 0

def test_palabra_pierde_puntaje():
    # Si arriesga palabra y pierde los intentos disponibles son 0.
    j = Juego('hola')
    j.intentosUsados = j.maxIntentos
    j.arriesgarPalabra('chau')
    assert j.finalizo() and j.puntaje() == 0

# Palabra con espacios.
def test_palabra_con_espacios_progreso():
    j = Juego("hola mundo")
    j.arriesgarLetra('o')
    assert j.mostrarProgresoPalabra() == '_o__ ____o'
