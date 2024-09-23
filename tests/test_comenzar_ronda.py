# Comenzar ronda
def test_comenzar_ronda_1(partida):
    partida.comenzar_ronda("palabra")
    assert partida.id_jugador_actual == 1
    assert partida.rondas == [0, 1]
    assert not partida.ronda_finalizo()


def test_comenzar_ronda_2(partida):
    partida.comenzar_ronda("palabra")
    partida.comenzar_ronda("palabra")
    assert partida.id_jugador_actual == 0
    assert partida.rondas == [1, 1]
    assert not partida.ronda_finalizo()


def test_comenzar_ronda_3(partida):
    partida.comenzar_ronda("palabra")
    partida.comenzar_ronda("palabra")
    partida.comenzar_ronda("palabra")
    assert partida.id_jugador_actual == 1
    assert partida.rondas == [1, 2]
    assert not partida.ronda_finalizo()


def test_comenzar_ronda_4(partida):
    partida.comenzar_ronda("palabra")
    partida.comenzar_ronda("palabra")
    partida.comenzar_ronda("palabra")
    partida.comenzar_ronda("palabra")
    assert partida.id_jugador_actual == 0
    assert partida.rondas == [2, 2]
    assert not partida.ronda_finalizo()
