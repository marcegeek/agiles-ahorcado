import pytest
from juego import Juego

def test_letra_invalida():
    j = Juego("palabra")
    resultado = j.arriesgarLetra("-")
    assert resultado == "letra invalida"
    
def test_letra_ya_usada():
    j = Juego("palabra")
    resultado = j.arriesgarLetra("h")
    resultado = j.arriesgarLetra("H")
    assert resultado == "letra ya usada"
    resultado = j.arriesgarLetra("a")
    resultado = j.arriesgarLetra("A")
    assert resultado == "letra ya usada"
    
def test_letra_no_esta():
    j = Juego("palabra")
    resultado = j.arriesgarLetra("x")
    assert resultado == "letra no se encuentra"
    
def test_letra_esta():
    j = Juego("palabra")
    resultado = j.arriesgarLetra('b')
    assert resultado == "letra se encuentra"
    
def test_letra_descontar_intento():
    j = Juego("palabra")
    j.arriesgarLetra('z')
    assert j.intentosUsados == j.intentosLetra
    assert j.intentosDisponibles() == max(j.maxIntentos - j.intentosUsados,0)
    