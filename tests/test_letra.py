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
    resultado = j.arriesgarLetra("b")
    assert resultado == "letra se encuentra"


def test_letra_esta_progreso():
    # Si la letra se encuentra el progreso debe cambiar.
    j = Juego("palabra")
    j.arriesgarLetra("b")
    assert j.mostrarProgresoPalabra() == "____b__"


def test_letra_esta_intentos():
    # Si la letra se encuentra el nro de intentos debe mantenerse.
    j = Juego("palabra")
    j.arriesgarLetra("b")
    assert j.intentosDisponibles() == j.maxIntentos


# Letra pierde
def test_letra_pierde_perdio():
    # Si arriesga maxIntentos veces y pierde perdio() debe ser True
    j = Juego("palabra")
    j.intentosUsados = j.maxIntentos
    j.arriesgarLetra("x")
    assert j.perdio()


def test_letra_pierde_finalizo():
    # Si arriesga maxIntentos veces y pierde finalizo() debe ser True
    j = Juego("palabra")
    j.intentosUsados = j.maxIntentos
    j.arriesgarLetra("x")
    assert j.finalizo()


def test_letra_pierde_mensaje():
    # Si arriesga maxIntentos veces y pierde el mensaje debe ser "letra no se encuentra"
    j = Juego("palabra")
    resultado = " "
    j.intentosUsados = j.maxIntentos
    resultado = j.arriesgarLetra("x")
    assert resultado == "letra no se encuentra"


def test_letra_pierde_intentos():
    # Si arriesga maxIntentos veces el nro de intentos debe ser 0.
    j = Juego("palabra")
    j.intentosUsados = j.maxIntentos
    j.arriesgarLetra("x")
    assert j.intentosDisponibles() == 0


def test_letra_pierde_puntaje():
    j = Juego("palabra")
    j.intentosUsados = j.maxIntentos
    j.arriesgarLetra("x")
    assert j.finalizo() and j.puntaje() == 0


# Letra gana
def test_letra_gana_finalizo():
    # Si adivina la palabra finalizo() debe ser True
    j = Juego("celu")
    j.arriesgarLetra("c")
    j.arriesgarLetra("e")
    j.arriesgarLetra("l")
    j.arriesgarLetra("u")
    assert j.finalizo()


def test_letra_gana_mensaje():
    # Si adivina la palabra el mensaje debe ser "letra se encuentra" y acerto=True.
    j = Juego("celu")
    j.arriesgarLetra("c")
    j.arriesgarLetra("e")
    j.arriesgarLetra("l")
    resultado = ""
    resultado = j.arriesgarLetra("u")
    assert resultado == "letra se encuentra"
    assert j.acerto


def test_letra_gana_progreso():
    # Si adivina la palabra el progreso esta completo
    j = Juego("celu")
    j.arriesgarLetra("c")
    j.arriesgarLetra("e")
    j.arriesgarLetra("l")
    j.arriesgarLetra("u")
    assert j.mostrarProgresoPalabra() == "celu"


def test_letra_gana_sin_errores_puntaje():
    j = Juego("celu")
    j.arriesgarLetra("c")
    j.arriesgarLetra("e")
    j.arriesgarLetra("l")
    j.arriesgarLetra("u")
    assert j.finalizo() and j.puntaje() == j.maxIntentos


def test_letra_gana_un_error_puntaje():
    j = Juego("celu")
    j.arriesgarLetra("x")
    j.arriesgarLetra("c")
    j.arriesgarLetra("e")
    j.arriesgarLetra("l")
    j.arriesgarLetra("u")
    assert j.finalizo() and j.puntaje() == j.maxIntentos - 1


def test_letra_gana_dos_errores_puntaje():
    j = Juego("celu")
    j.arriesgarLetra("x")
    j.arriesgarLetra("c")
    j.arriesgarLetra("e")
    j.arriesgarLetra("y")
    j.arriesgarLetra("l")
    j.arriesgarLetra("u")
    assert j.finalizo() and j.puntaje() == j.maxIntentos - 2


def test_letra_gana_ultimo_intento_puntaje():
    j = Juego("celu")
    j.intentosUsados = j.maxIntentos - 1
    j.arriesgarLetra("c")
    j.arriesgarLetra("e")
    j.arriesgarLetra("l")
    j.arriesgarLetra("u")
    assert j.finalizo() and j.puntaje() == 1


# Letras usadas
def test_letras_usadas():
    j = Juego("palabra")
    j.arriesgarLetra("a")
    j.arriesgarLetra("b")
    j.arriesgarLetra("c")
    j.arriesgarLetra("d")
    j.arriesgarLetra("e")
    j.arriesgarLetra("l")
    assert j.letrasUsadas == ["a", "b", "c", "d", "e", "l"]


# Juego en curso
def test_letra_juego_en_curso_finalizo():
    j = Juego("hola")
    j.arriesgarLetra("e")
    j.arriesgarLetra("a")
    assert not j.finalizo()


def test_letra_juego_en_curso_puntaje():
    j = Juego("hola")
    j.arriesgarLetra("e")
    j.arriesgarLetra("a")
    assert j.puntaje() == 0
