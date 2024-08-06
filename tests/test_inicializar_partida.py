from juego import Partida

# Inicializar partida
def test_inicializar_partida_rondas():
    j = Partida()
    assert j.rondas == [0, 0]

def test_inicializar_partida_jugador():
    j = Partida()
    assert j.idJugadorActual is None

def test_inicializar_partida_finalizo():
    j = Partida()
    assert not j.finalizo

def test_inicializar_partida_puntos():
    j = Partida()
    assert j.puntos() == [0, 0]
    assert j.puntosJugador(0) == 0
    assert j.puntosJugador(1) == 0
