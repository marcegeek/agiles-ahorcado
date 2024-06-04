import pytest
from juego import Juego

def test_letra_invalida():
    juego = Juego("palabra")
    resultado = juego.arriesgar_letra("-")
    assert resultado == "letra invalida"
    
def test_letra_ya_usada():
    juego = Juego("palabra")
    resultado = juego.arriesgar_letra("a")
    resultado = juego.arriesgar_letra("A")
    assert resultado == "letra ya usada"
    
def test_letra_no_esta():
    juego = Juego("palabra")
    resultado = juego.arriesgar_letra("x")
    assert resultado == "letra no se encuentra"
    
def test_letra_esta():
    juego = Juego("palabra")
    resultado = juego.arriesgar_letra("b")
    assert resultado == "letra se encuentra"