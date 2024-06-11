import pytest
from juego import Juego

def test_reiniciar_juego():
    j = Juego("hola")
    j.arriesgarLetra('h')
    j.arriesgarLetra('o')
    j.arriesgarLetra('x')
    j.__init__("nuevo")  # Reiniciar el juego con una nueva palabra
    assert j.palabra == "nuevo"
    assert j.intentosUsados == 0
    assert j.letrasUsadas == []
    assert j.mostrarAvance() == '_____'
    