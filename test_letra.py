import pytest
from juego import Juego

def test_letra_invalida():
    # Si la letra es invalida, el nro de intentos y el avance deberian mantenerse. Y el mensaje "letra invalida".
    j = Juego("palabra")
    resultado = j.arriesgarLetra(" ")
    
    assert j.intentosDisponibles() == j.maxIntentos
    assert j.mostrarAvance() == '_______'
    assert resultado == "letra invalida"
    
def test_letra_ya_usada():
    # Si la letra ya fue usada, el nro de intentos y el avance deberian mantenerse. Y el mensaje "letra ya usada".
    j = Juego("palabra")
    resultado = j.arriesgarLetra("h")
    resultado = j.arriesgarLetra("H")
    assert j.intentosDisponibles() == j.maxIntentos-1
    assert j.mostrarAvance() == '_______'
    assert resultado == "letra ya usada"
    
    resultado = j.arriesgarLetra("a")
    resultado = j.arriesgarLetra("A")
    assert j.intentosDisponibles() == j.maxIntentos-1
    assert j.mostrarAvance() == '_a_a__a'
    assert resultado == "letra ya usada"
    
def test_letra_no_esta():
    # Si la letra no se encuentra, el nro de intentos deberia bajar, el avance mantenerse y el mensaje "letra no se encuentra"
    j = Juego("palabra")
    resultado = j.arriesgarLetra("x")
    assert j.intentosDisponibles() == j.maxIntentos-1
    assert j.mostrarAvance() == '_______'
    assert resultado == "letra no se encuentra"
    
def test_letra_esta():
    # Si la letra se encuentra, el nro de intentos deberia mantenerse, el avance cambiar y el mensaje "letra se encuentra"
    j = Juego("palabra")
    resultado = j.arriesgarLetra('b')
    assert j.intentosDisponibles() == j.maxIntentos
    assert j.mostrarAvance() == '____b__'
    assert resultado == "letra se encuentra"
    
def test_letra_pierde():
    # Si arriesga maxIntentos veces y pierde el mensaje debe ser "pierde"
    j = Juego("palabra")
    resultado = ' '
    j.intentosUsados = j.maxIntentos
    resultado = j.arriesgarLetra('x')
    assert resultado == 'pierde'
    
def test_letra_gana():
    j = Juego("celu")
    j.arriesgarLetra('c')
    j.arriesgarLetra('e')
    j.arriesgarLetra('l')
    resultado = ''
    resultado = j.arriesgarLetra('u')        
    assert resultado == "ganaste" 
    