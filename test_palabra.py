from juego import Juego


def test_palabra_acierta():
    j = Juego('zapato')
    j.arriesgar_palabra('zapato')
    assert j.acierta()
    j = Juego('zapato')
    j.arriesgar_palabra('ZApaTo')
    assert j.acierta()
    j = Juego('ZApato')
    j.arriesgar_palabra('zapato')
    assert j.acierta()


def test_palabra_pierde():
    j = Juego('zapato')
    assert j.intentos_disponibles() == 6
    j.arriesgar_palabra('tapado')
    assert j.intentos_disponibles() == 4
    assert not j.acierta()
    j.arriesgar_palabra('rapado')
    assert not j.acierta()
    j.arriesgar_palabra('papado')
