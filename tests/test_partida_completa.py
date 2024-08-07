from .util import partida, ronda_completa


def test_partida_finaliza_una_ronda(partida):
    ronda_completa(partida, False)
    assert not partida.finalizo()


def test_partida_finaliza_dos_rondas(partida):
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    assert not partida.finalizo()


def test_partida_finaliza_dos_rondas(partida):
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    assert not partida.finalizo()


def test_partida_finaliza_diez_rondas(partida):
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    assert not partida.finalizo()


def test_partida_finaliza_once_rondas(partida):
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    assert not partida.finalizo()


def test_partida_finaliza_doce_rondas(partida):
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    ronda_completa(partida, False)
    assert partida.finalizo()
