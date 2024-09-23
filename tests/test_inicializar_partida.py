import pytest

from ahorcado import Partida


@pytest.fixture
def partida():
    return Partida()


# Inicializar partida
def test_inicializar_partida_rondas(partida):
    assert partida.rondas == [0, 0]


def test_inicializar_partida_jugador(partida):
    assert partida.id_jugador_actual is None


def test_inicializar_partida_finalizo(partida):
    assert not partida.finalizo()


def test_inicializar_partida_ronda_finalizo(partida):
    assert not partida.ronda_finalizo()


def test_inicializar_partida_puntos(partida):
    assert partida.puntos == [0, 0]
    assert partida.puntos_jugador(0) == 0
    assert partida.puntos_jugador(1) == 0


def test_inicializar_partida_actualizar_puntos(partida):
    with pytest.raises(Exception, match="No se puede actualizar puntos si no se inició ninguna ronda"):
        partida.actualizar_puntos()


def test_inicializar_partida_data_rondas(partida_data):
    assert partida_data().rondas == [0, 0]


def test_inicializar_partida_data_jugador(partida_data):
    assert partida_data().id_jugador_actual is None
