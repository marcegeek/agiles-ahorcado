import pytest
from unittest.mock import Mock

from juego import Juego, Partida


def mock_juego():
    j = Mock(spec=Juego)
    j.acerto = False
    j.perdio.return_value = False
    j.finalizo.return_value = False
    return j


def mock_juego_pierde():
    j = mock_juego()
    j.perdio.return_value = True
    j.finalizo.return_value = True
    return j


def mock_juego_gana():
    j = mock_juego()
    j.acerto = True
    j.finalizo.return_value = True
    return j


@pytest.fixture
def partida():
    return Partida()


# Simular una ronda completa, ganando o perdiendo la misma
def ronda_completa(partida, gana):
    partida.comenzarRonda("palabra")
    # reemplazamos el juego por un mock con el comportamiento a simular
    if gana:
        partida.juego = mock_juego_gana()
    else:
        partida.juego = mock_juego_pierde()
    partida.actualizarAciertos()
