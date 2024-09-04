import pytest
from juego import Partida


@pytest.fixture
def partida():
    return Partida()


# Inicializar partida
def test_inicializar_partida_rondas(partida):
    assert partida.rondas == [0, 0]


def test_inicializar_partida_jugador(partida):
    assert partida.idJugadorActual is None


def test_inicializar_partida_finalizo(partida):
    assert not partida.finalizo()


def test_inicializar_partida_ronda_finalizo(partida):
    assert not partida.rondaFinalizo()


def test_inicializar_partida_puntos(partida):
    assert partida.puntos == [0, 0]
    assert partida.puntosJugador(0) == 0
    assert partida.puntosJugador(1) == 0
