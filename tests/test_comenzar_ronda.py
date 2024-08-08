# Comenzar ronda
def test_comenzar_ronda_1(partida):
    partida.comenzarRonda("palabra")
    assert partida.idJugadorActual == 0
    assert partida.rondas == [1, 0]
    assert not partida.rondaFinalizo()

def test_comenzar_ronda_2(partida):
    partida.comenzarRonda("palabra")
    partida.comenzarRonda("palabra")
    assert partida.idJugadorActual == 1
    assert partida.rondas == [1, 1]
    assert not partida.rondaFinalizo()

def test_comenzar_ronda_3(partida):
    partida.comenzarRonda("palabra")
    partida.comenzarRonda("palabra")
    partida.comenzarRonda("palabra")
    assert partida.idJugadorActual == 0
    assert partida.rondas == [2, 1]
    assert not partida.rondaFinalizo()

def test_comenzar_ronda_4(partida):
    partida.comenzarRonda("palabra")
    partida.comenzarRonda("palabra")
    partida.comenzarRonda("palabra")
    partida.comenzarRonda("palabra")
    assert partida.idJugadorActual == 1
    assert partida.rondas == [2, 2]
    assert not partida.rondaFinalizo()
