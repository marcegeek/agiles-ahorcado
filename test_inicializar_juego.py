from juego import Juego

# Inicializar juego
def test_inicializacion_juego_progreso():
    j = Juego("palabra")
    assert j.mostrarProgresoPalabra() == "_______"

def test_inicializacion_juego_intentos():
    j = Juego("palabra")
    assert j.intentosDisponibles() == j.maxIntentos
    
def test_inicializacion_juego_letras_usadas():
    j = Juego("palabra")
    assert j.letrasUsadas == []