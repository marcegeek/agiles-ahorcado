from juego import Juego

# Letra invalida.
def test_letra_invalida_mensaje():
    # Si la letra es invalida el mensaje es "letra invalida".
    j = Juego("palabra")
    resultado = j.arriesgarLetra("#")
    assert resultado == "letra invalida"
    
def test_letra_invalida_progreso():
    # Si la letra es invalida el progreso deberia mantenerse.
    j = Juego("palabra")
    resultado = j.arriesgarLetra("#")
    assert j.mostrarProgresoPalabra() == "_______"

def test_letra_invalida_intentos():
    # Si la letra es invalida el nro de intentos deberia mantenerse.
    j = Juego("palabra")
    resultado = j.arriesgarLetra("#")
    assert j.intentosDisponibles() == j.maxIntentos


# Letra ya usada
def test_letra_ya_usada_mensaje():
    # Si la letra ya fue usada el mensaje es "letra ya usada".
    j = Juego("palabra")
    resultado = j.arriesgarLetra("h")
    resultado = j.arriesgarLetra("H")
    assert resultado == "letra ya usada"
    
def test_letra_ya_usada_progreso():
    # Si la letra es invalida el progreso deberia mantenerse.
    j = Juego("palabra")
    j.arriesgarLetra("a")
    j.arriesgarLetra("A")
    assert j.mostrarProgresoPalabra() == "_a_a__a"
    
def test_letra_ya_usada():
    # Si la letra es invalida el nro de intentos deberia mantenerse.
    j = Juego("palabra")
    j.arriesgarLetra("h")
    j.arriesgarLetra("H")
    assert j.intentosDisponibles() == j.maxIntentos - j.intentosLetra

# Letra no esta  
def test_letra_no_esta_mensaje():
    # Si la letra no se encuentra, el nro de intentos deberia bajar, el avance mantenerse y el mensaje "letra no se encuentra"
    j = Juego("palabra")
    resultado = j.arriesgarLetra("x")
    assert resultado == "letra no se encuentra"

def test_letra_no_esta_progreso():
    # Si la letra no se encuentra, el nro de intentos deberia bajar, el avance mantenerse y el mensaje "letra no se encuentra"
    j = Juego("palabra")
    resultado = j.arriesgarLetra("x")
    assert resultado == "letra no se encuentra"

def test_letra_no_esta():
    # Si la letra no se encuentra, el nro de intentos deberia bajar, el avance mantenerse y el mensaje "letra no se encuentra"
    j = Juego("palabra")
    resultado = j.arriesgarLetra("x")
    assert resultado == "letra no se encuentra"
    
def test_letra_esta():
    # Si la letra se encuentra, el nro de intentos deberia mantenerse, el avance cambiar y el mensaje "letra se encuentra"
    j = Juego("palabra")
    resultado = j.arriesgarLetra('b')
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
    