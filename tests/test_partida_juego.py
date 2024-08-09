def test_ronda_gana_finaliza(partida, ronda_completa):
    ronda_completa(True, 1)
    assert partida.rondaFinalizo()


def test_ronda_pierde_finaliza(partida, ronda_completa):
    ronda_completa(False)
    assert partida.rondaFinalizo()


def test_puntos_un_acierto(partida, ronda_completa):
    ronda_completa(True, 1)
    assert partida.rondaFinalizo()
    assert partida.puntos == [1, 0]


def test_puntos_fallo_acierto(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True, 3)
    assert partida.rondaFinalizo()
    assert partida.puntos == [0, 3]
    assert partida.puntosJugador(0) == 0
    assert partida.puntosJugador(1) == 3


def test_puntos_fallo_fallo_acierto(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(True, 2)
    assert partida.puntos == [2, 0]
    assert partida.puntosJugador(0) == 2
    assert partida.puntosJugador(1) == 0


def test_puntos_uno_y_uno(partida, ronda_completa):
    ronda_completa(True, 1)
    ronda_completa(True, 1)
    assert partida.rondaFinalizo()
    assert partida.puntos == [1, 1]
    assert partida.puntosJugador(0) == 1
    assert partida.puntosJugador(1) == 1


def test_puntos_acierto_fallo_acierto(partida, ronda_completa):
    ronda_completa(True, 3)
    ronda_completa(False)
    ronda_completa(True, 4)
    assert partida.puntos == [7, 0]
    assert partida.puntosJugador(0) == 7
    assert partida.puntosJugador(1) == 0


def test_puntos_tres_aciertos(partida, ronda_completa):
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 3)
    assert partida.puntos == [4, 2]
    assert partida.puntosJugador(0) == 4
    assert partida.puntosJugador(1) == 2


def test_puntos_cuatro_aciertos(partida, ronda_completa):
    ronda_completa(True, 4)
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 1)
    assert partida.puntos == [6, 2]
    assert partida.puntosJugador(0) == 6
    assert partida.puntosJugador(1) == 2


def test_puntos_fallo_acierto_fallo_acierto(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(False)
    ronda_completa(True, 6)
    assert partida.puntos == [0, 7]
    assert partida.puntosJugador(0) == 0
    assert partida.puntosJugador(1) == 7


def test_puntos_fallo_y_tres_aciertos(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True, 1)
    ronda_completa(True, 2)
    ronda_completa(True, 5)
    assert partida.puntos == [2, 6]
    assert partida.puntosJugador(0) == 2
    assert partida.puntosJugador(1) == 6
