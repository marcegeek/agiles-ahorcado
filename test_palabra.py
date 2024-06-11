from juego import Juego


def test_palabra_acierta():
    j = Juego('hola')
    resultado = j.arriesgarPalabra('hola')
    assert resultado == "ganaste"
    assert j.mostrarAvance() == "hola"

def test_palabra_descontar_intento():
    j = Juego('hola')
    j.arriesgarPalabra('chau')
    assert j.intentosUsados == j.intentosPalabra
    assert j.intentosDisponibles() == max(j.maxIntentos - j.intentosUsados,0)
    assert j.mostrarAvance() == '____'

def test_palabra_pierde():
    j = Juego('hola')
    j.intentosUsados = j.maxIntentos
    resultado = j.arriesgarPalabra('chau')
    assert resultado == 'perdiste'
    assert j.mostrarAvance() == "____"
    
def test_palabra_con_espacios():
    j = Juego("hola mundo")
    resultado = j.arriesgarLetra('o')
    assert resultado == "letra se encuentra"
    assert j.mostrarAvance() == '_o__ ____o'
    assert j.intentosDisponibles() == j.maxIntentos