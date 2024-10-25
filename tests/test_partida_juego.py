from .conftest import mock_juego_gana


def test_ronda_gana_finaliza(partida, ronda_completa):
    ronda_completa(True, 1)
    assert partida.ronda_finalizo()


def test_ronda_pierde_finaliza(partida, ronda_completa):
    ronda_completa(False)
    assert partida.ronda_finalizo()


def test_puntos_un_acierto(partida, ronda_completa):
    ronda_completa(True, 1)
    assert partida.ronda_finalizo()
    assert partida.puntos == [0, 1]


def test_puntos_fallo_acierto(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True, 3)
    assert partida.ronda_finalizo()
    assert partida.puntos == [3, 0]
    assert partida.puntos_jugador(0) == 3
    assert partida.puntos_jugador(1) == 0


def test_puntos_fallo_fallo_acierto(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(True, 2)
    assert partida.puntos == [0, 2]
    assert partida.puntos_jugador(0) == 0
    assert partida.puntos_jugador(1) == 2


def test_puntos_uno_y_uno(partida, ronda_completa):
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    assert partida.ronda_finalizo()
    assert partida.puntos == [1, 1]
    assert partida.puntos_jugador(0) == 1
    assert partida.puntos_jugador(1) == 1


def test_puntos_acierto_fallo_acierto(partida, ronda_completa):
    ronda_completa(True, 3)
    ronda_completa(False)
    ronda_completa(True, 4)
    assert partida.puntos == [0, 7]
    assert partida.puntos_jugador(0) == 0
    assert partida.puntos_jugador(1) == 7


def test_puntos_tres_aciertos(partida, ronda_completa):
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 3)
    assert partida.puntos == [2, 4]
    assert partida.puntos_jugador(0) == 2
    assert partida.puntos_jugador(1) == 4


def test_puntos_cuatro_aciertos(partida, ronda_completa):
    ronda_completa(True, 4)
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 1)
    assert partida.puntos == [2, 6]
    assert partida.puntos_jugador(0) == 2
    assert partida.puntos_jugador(1) == 6


def test_puntos_fallo_acierto_fallo_acierto(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(False)
    ronda_completa(True, 6)
    assert partida.puntos == [7, 0]
    assert partida.puntos_jugador(0) == 7
    assert partida.puntos_jugador(1) == 0


def test_puntos_fallo_y_tres_aciertos(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 5)
    assert partida.puntos == [6, 2]
    assert partida.puntos_jugador(0) == 6
    assert partida.puntos_jugador(1) == 2


def test_puntos_actualizar_puntos(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(False)
    partida.juego = mock_juego_gana(1)
    partida.actualizar_puntos()
    partida.actualizar_puntos()
    ronda_completa(True, 2)
    partida.actualizar_puntos()
    partida.actualizar_puntos()
    ronda_completa(True, 5)
    assert partida.puntos == [6, 2]
    assert partida.puntos_jugador(0) == 6
    assert partida.puntos_jugador(1) == 2


def test_partida_no_finaliza_ganador(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 5)
    assert partida.ganador() is None


def test_partida_no_finaliza_empate(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 5)
    assert partida.empate() is None


def test_partida_ganador_0(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 5)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    assert partida.ganador() == 0


def test_partida_ganador_0_empate(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 5)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    assert partida.empate() is not None
    assert not partida.empate()


def test_partida_ganador_1(partida, ronda_completa):
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 5)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    assert partida.ganador() == 1


def test_partida_ganador_1_empate(partida, ronda_completa):
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 5)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    assert partida.empate() is not None
    assert not partida.empate()


def test_partida_ganador_empate(partida, ronda_completa):
    ronda_completa(True, 3)
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 5)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    assert partida.ganador() == -1
    assert partida.empate()


def test_ronda_gana_finaliza_data(ronda_completa, partida_data):
    ronda_completa(True, 1)
    assert partida_data().ronda_finalizo()


def test_puntos_fallo_acierto_data(ronda_completa, partida_data):
    ronda_completa(False)
    ronda_completa(True, 3)
    p = partida_data()
    assert p.ronda_finalizo()
    assert p.puntos == [3, 0]
    assert p.puntos_jugador(0) == 3
    assert p.puntos_jugador(1) == 0
