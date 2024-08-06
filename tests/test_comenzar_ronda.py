from juego import Partida
import pytest


@pytest.fixture
def partida():
    return Partida()


# Comenzar ronda
def test_comenzar_ronda_jugador0(partida):
    partida.comenzarRonda("palabra")
    assert partida.idJugadorActual == 0
    assert partida.rondas == [1, 0]

def test_comenzar_ronda_jugador1(partida):
    partida.comenzarRonda("palabra")
    partida.idJugadorActual = 1
    partida.comenzarRonda("palabra")
    assert partida.idJugadorActual == 1
    assert partida.rondas == [1, 1]
