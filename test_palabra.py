from juego import Juego


def test_palabra_acierta():
    j = Juego('hola')
    resultado = j.arriesgarPalabra('hola')
    assert resultado == "ganaste"

def test_palabra_descontar_intento():
    j = Juego('hola')
    j.arriesgarPalabra('chau')
    assert j.intentosUsados == j.intentosPalabra
    assert j.intentosDisponibles() == max(j.maxIntentos - j.intentosUsados,0)

def test_palabra_pierde():
    j = Juego('hola')
    assert j.intentosDisponibles() == j.maxIntentos
    while(j.maxIntentos - j.intentosUsados > 0):
        j.arriesgarPalabra('chau')
        assert j.intentosDisponibles() == max(j.maxIntentos - j.intentosUsados,0)
        
    resultado = j.arriesgarPalabra('chau')
    assert resultado == 'perdiste'