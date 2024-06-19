from juego import Juego

# Palabra acierta
def test_palabra_acierta_mensaje():
    # Si adivina la palabra el mensaje es "ganaste".
    j = Juego('hola')
    resultado = j.arriesgarPalabra('hola')
    assert resultado == "ganaste"

def test_palabra_acierta_progreso():
    # Si adivina la palabra el progreso esta completo.
    j = Juego('hola')
    j.arriesgarPalabra('hola')
    assert j.mostrarProgresoPalabra() == "hola"

# Palabra incorrecta
def test_palabra_incorrecta_mensaje():
    j = Juego('hola')
    resultado = j.arriesgarPalabra('chau')
    assert resultado == "palabra incorrecta"
    assert j.intentosUsados == j.intentosPalabra
    assert j.intentosDisponibles() == max(j.maxIntentos - j.intentosUsados,0)
    assert j.mostrarProgresoPalabra() == '____'

def test_palabra_pierde():
    j = Juego('hola')
    j.intentosUsados = j.maxIntentos
    resultado = j.arriesgarPalabra('chau')
    assert resultado == 'perdiste'
    assert j.mostrarProgresoPalabra() == "____"
    
def test_palabra_con_espacios():
    j = Juego("hola mundo")
    resultado = j.arriesgarLetra('o')
    assert resultado == "letra se encuentra"
    assert j.mostrarProgresoPalabra() == '_o__ ____o'
    assert j.intentosDisponibles() == j.maxIntentos