import pytest
from unittest.mock import Mock

from juego import Juego, Partida


def mock_juego():
    j = Mock(spec=Juego)
    j.acerto = False
    j.perdio.return_value = False
    j.finalizo.return_value = False
    j.puntaje.return_value = 0
    return j


def mock_juego_pierde():
    j = mock_juego()
    j.perdio.return_value = True
    j.finalizo.return_value = True
    return j


def mock_juego_gana(puntaje):
    j = mock_juego()
    j.acerto = True
    j.finalizo.return_value = True
    j.puntaje.return_value = puntaje
    return j


@pytest.fixture
def partida():
    return Partida()


@pytest.fixture
def ronda_completa(partida):
    # Simular una ronda completa, ganando o perdiendo la misma
    def _ronda_completa(gana, puntaje=None):
        partida.comenzarRonda("palabra")
        # reemplazamos el juego por un mock con el comportamiento a simular
        if gana:
            if puntaje is None:
                pytest.fail("puntaje requerido para ronda_completa ganadora")
            partida.juego = mock_juego_gana(puntaje)
        else:
            partida.juego = mock_juego_pierde()
        partida.actualizarPuntos()

    # devuelve la función para efectuar la ronda
    return _ronda_completa
