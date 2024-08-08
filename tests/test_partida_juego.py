def test_ronda_gana_finaliza(partida, ronda_completa):
    ronda_completa(True)
    assert partida.rondaFinalizo()


def test_ronda_pierde_finaliza(partida, ronda_completa):
    ronda_completa(False)
    assert partida.rondaFinalizo()


def test_aciertos_un_acierto(partida, ronda_completa):
    ronda_completa(True)
    assert partida.rondaFinalizo()
    assert partida.aciertos == [1, 0]


def test_aciertos_fallo_acierto(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True)
    assert partida.rondaFinalizo()
    assert partida.aciertos == [0, 1]


def test_aciertos_fallo_fallo_acierto(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(True)
    assert partida.aciertos == [1, 0]


def test_aciertos_uno_y_uno(partida, ronda_completa):
    ronda_completa(True)
    ronda_completa(True)
    assert partida.rondaFinalizo()
    assert partida.aciertos == [1, 1]


def test_aciertos_acierto_fallo_acierto(partida, ronda_completa):
    ronda_completa(True)
    ronda_completa(False)
    ronda_completa(True)
    assert partida.aciertos == [2, 0]


def test_aciertos_tres_aciertos(partida, ronda_completa):
    ronda_completa(True)
    ronda_completa(True)
    ronda_completa(True)
    assert partida.aciertos == [2, 1]


def test_aciertos_cuatro_aciertos(partida, ronda_completa):
    ronda_completa(True)
    ronda_completa(True)
    ronda_completa(True)
    ronda_completa(True)
    assert partida.aciertos == [2, 2]


def test_aciertos_fallo_acierto_fallo_acierto(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True)
    ronda_completa(False)
    ronda_completa(True)
    assert partida.aciertos == [0, 2]


def test_aciertos_fallo_y_tres_aciertos(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True)
    ronda_completa(True)
    ronda_completa(True)
    assert partida.aciertos == [1, 2]


def test_puntos_dos_aciertos(partida, ronda_completa):
    ronda_completa(True)
    ronda_completa(True)
    assert partida.puntos() == [100, 100]
    assert partida.puntosJugador(0) == 100
    assert partida.puntosJugador(1) == 100


def test_puntos_fallo_acierto(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True)
    assert partida.puntos() == [0, 100]
    assert partida.puntosJugador(0) == 0
    assert partida.puntosJugador(1) == 100


def test_puntos_fallo_y_tres_aciertos(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(True)
    ronda_completa(True)
    ronda_completa(True)
    assert partida.puntos() == [100, 200]
    assert partida.puntosJugador(0) == 100
    assert partida.puntosJugador(1) == 200


def test_puntos_acierto_fallo_tres_aciertos_y_fallo(partida, ronda_completa):
    ronda_completa(True)
    ronda_completa(False)
    ronda_completa(True)
    ronda_completa(True)
    ronda_completa(True)
    ronda_completa(False)
    assert partida.puntos() == [300, 100]
    assert partida.puntosJugador(0) == 300
    assert partida.puntosJugador(1) == 100
