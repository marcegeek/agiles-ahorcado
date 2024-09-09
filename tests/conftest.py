import pytest
from unittest.mock import Mock

from juego import Juego, Partida


@pytest.fixture
def juego_data():
    # Recrear un juego a partir de su serialización, empleando los datos suministrados
    def _juego_data(palabra, acerto=False, intentosUsados=0, letrasUsadas=[]):
        j = Juego(palabra)
        j.acerto = acerto
        j.intentosUsados = intentosUsados
        j.letrasUsadas = letrasUsadas
        return Juego(data=j.to_dict())

    return _juego_data


def mock_juego():
    j = Mock(spec=Juego)
    j.acerto = False
    j.perdio.return_value = False
    j.finalizo.return_value = False
    j.puntaje.return_value = 0
    j.to_dict.return_value = {
        "palabra": "palabra",
        "acerto": False,
        "intentosUsados": 0,
        "letrasUsadas": [],
    }
    return j


def mock_juego_pierde():
    j = mock_juego()
    j.perdio.return_value = True
    j.finalizo.return_value = True
    j.to_dict.return_value = {
        "palabra": "palabra",
        "acerto": False,
        "intentosUsados": 6,
        "letrasUsadas": ["m", "n", "o", "q", "s", "t"],
    }
    return j


def mock_juego_gana(puntaje):
    j = mock_juego()
    j.acerto = True
    j.finalizo.return_value = True
    j.puntaje.return_value = puntaje
    j.to_dict.return_value = {
        "palabra": "palabra",
        "acerto": True,
        "intentosUsados": 6 - puntaje,
        "letrasUsadas": ["a", "b", "l", "p", "r"],
    }
    return j


@pytest.fixture
def partida():
    return Partida()


@pytest.fixture
def partida_data(partida):
    # Recrear la partida a partir de su serialización
    def _partida_data():
        return Partida(data=partida.to_dict())

    return _partida_data


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
