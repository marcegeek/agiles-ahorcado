def test_partida_finaliza_una_ronda(partida, ronda_completa):
    ronda_completa(False)
    assert not partida.finalizo()


def test_partida_finaliza_dos_rondas(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(False)
    assert not partida.finalizo()


def test_partida_finaliza_dos_rondas(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(False)
    assert not partida.finalizo()


def test_partida_finaliza_diez_rondas(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    assert not partida.finalizo()


def test_partida_finaliza_once_rondas(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    assert not partida.finalizo()


def test_partida_finaliza_doce_rondas(partida, ronda_completa):
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    ronda_completa(False)
    assert partida.finalizo()
