from juego import Juego

# Letra invalida.
def test_letra_invalida_mensaje():
    # Si la letra es invalida el mensaje es "letra invalida".
    j = Juego("palabra")
    resultado = j.arriesgarLetra("#")
    assert resultado == "letra invalida"
    
def test_letra_invalida_progreso():
    # Si la letra es invalida el progreso debe mantenerse.
    j = Juego("palabra")
    j.arriesgarLetra("#")
    assert j.mostrarProgresoPalabra() == "_______"

def test_letra_invalida_intentos():
    # Si la letra es invalida el nro de intentos debe mantenerse.
    j = Juego("palabra")
    j.arriesgarLetra("#")
    assert j.intentosDisponibles() == j.maxIntentos


# Letra ya usada
def test_letra_ya_usada_mensaje():
    # Si la letra ya fue usada el mensaje es "letra ya usada".
    j = Juego("palabra")
    resultado = j.arriesgarLetra("h")
    resultado = j.arriesgarLetra("H")
    assert resultado == "letra ya usada"
    
def test_letra_ya_usada_progreso():
    # Si la letra es invalida el progreso debe mantenerse.
    j = Juego("palabra")
    j.arriesgarLetra("a")
    j.arriesgarLetra("A")
    assert j.mostrarProgresoPalabra() == "_a_a__a"
    
def test_letra_ya_usada():
    # Si la letra es invalida el nro de intentos debe mantenerse.
    j = Juego("palabra")
    j.arriesgarLetra("h")
    j.arriesgarLetra("H")
    assert j.intentosDisponibles() == j.maxIntentos - j.intentosLetra

# Letra no esta  
def test_letra_no_esta_mensaje():
    # Si la letra no se encuentra el mensaje "letra no se encuentra"
    j = Juego("palabra")
    resultado = j.arriesgarLetra("x")
    assert resultado == "letra no se encuentra"

def test_letra_no_esta_progreso():
    # Si la letra no se encuentra el progreso debe mantenerse.
    j = Juego("palabra")
    j.arriesgarLetra("x")
    assert j.mostrarProgresoPalabra() == "_______"

def test_letra_no_esta_intentos():
    # Si la letra no se encuentra el nro de intentos debe disminuir.
    j = Juego("palabra")
    j.arriesgarLetra("x")
    assert j.intentosDisponibles() == j.maxIntentos - j.intentosLetra

# Letra esta 
def test_letra_esta_mensaje():
    # Si la letra se encuentra el mensaje es "letra se encuentra".
    j = Juego("palabra")
    resultado = j.arriesgarLetra('b')
    assert resultado == "letra se encuentra"

def test_letra_esta_progreso():
    # Si la letra se encuentra el progreso debe cambiar.
    j = Juego("palabra")
    j.arriesgarLetra('b')
    assert j.mostrarProgresoPalabra() == "____b__"

def test_letra_esta_intentos():
    # Si la letra se encuentra el nro de intentos debe mantenerse.
    j = Juego("palabra")
    j.arriesgarLetra('b')
    assert j.intentosDisponibles() == j.maxIntentos

# Letra pierde
def test_letra_pierde_mensaje():
    # Si arriesga maxIntentos veces y pierde el mensaje debe ser "pierde"
    j = Juego("palabra")
    resultado = ' '
    j.intentosUsados = j.maxIntentos
    resultado = j.arriesgarLetra('x')
    assert resultado == 'pierde'

def test_letra_pierde_intentos():
    # Si arriesga maxIntentos veces y el nro de intentos debe ser 0.
    j = Juego("palabra")
    j.intentosUsados = j.maxIntentos
    j.arriesgarLetra('x')
    assert j.intentosDisponibles() == 0

# Letra gana  
def test_letra_gana_mensaje():
    # Si adivina la palabra el mensaje debe ser "ganaste".
    j = Juego("celu")
    j.arriesgarLetra('c')
    j.arriesgarLetra('e')
    j.arriesgarLetra('l')
    resultado = ''
    resultado = j.arriesgarLetra('u')        
    assert resultado == "ganaste" 
    
def test_letra_gana_progreso():
    # Si adivina la palabra el progreso esta completo
    j = Juego("celu")
    j.arriesgarLetra('c')
    j.arriesgarLetra('e')
    j.arriesgarLetra('l')
    j.arriesgarLetra('u')        
    assert j.mostrarProgresoPalabra() == "celu"
    