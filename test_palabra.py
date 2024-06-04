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
