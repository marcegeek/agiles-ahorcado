from ahorcado import Juego


# Letra invalida.
def test_letra_invalida_mensaje():
    # Si la letra es invalida el mensaje es "letra invalida".
    j = Juego("palabra")
    resultado = j.arriesgar_letra("#")
    assert resultado == "letra invalida"


def test_letra_invalida_progreso():
    # Si la letra es invalida el progreso debe mantenerse.
    j = Juego("palabra")
    j.arriesgar_letra("#")
    assert j.mostrar_progreso_palabra() == "_______"


def test_letra_invalida_intentos():
    # Si la letra es invalida el nro de intentos debe mantenerse.
    j = Juego("palabra")
    j.arriesgar_letra("#")
    assert j.intentos_disponibles() == Juego.MAX_INTENTOS


# Letra ya usada
def test_letra_ya_usada_mensaje():
    # Si la letra ya fue usada el mensaje es "letra ya usada".
    j = Juego("palabra")
    resultado = j.arriesgar_letra("h")
    resultado = j.arriesgar_letra("H")
    assert resultado == "letra ya usada"


def test_letra_ya_usada_progreso():
    # Si la letra es invalida el progreso debe mantenerse.
    j = Juego("palabra")
    j.arriesgar_letra("a")
    j.arriesgar_letra("A")
    assert j.mostrar_progreso_palabra() == "_a_a__a"


def test_letra_ya_usada():
    # Si la letra es invalida el nro de intentos debe mantenerse.
    j = Juego("palabra")
    j.arriesgar_letra("h")
    j.arriesgar_letra("H")
    assert j.intentos_disponibles() == Juego.MAX_INTENTOS - Juego.INTENTOS_LETRA


# Letra no esta
def test_letra_no_esta_mensaje():
    # Si la letra no se encuentra el mensaje "letra no se encuentra"
    j = Juego("palabra")
    resultado = j.arriesgar_letra("x")
    assert resultado == "letra no se encuentra"


def test_letra_no_esta_progreso():
    # Si la letra no se encuentra el progreso debe mantenerse.
    j = Juego("palabra")
    j.arriesgar_letra("x")
    assert j.mostrar_progreso_palabra() == "_______"


def test_letra_no_esta_intentos():
    # Si la letra no se encuentra el nro de intentos debe disminuir.
    j = Juego("palabra")
    j.arriesgar_letra("x")
    assert j.intentos_disponibles() == Juego.MAX_INTENTOS - Juego.INTENTOS_LETRA


# Letra esta
def test_letra_esta_mensaje():
    # Si la letra se encuentra el mensaje es "letra se encuentra".
    j = Juego("palabra")
    resultado = j.arriesgar_letra("b")
    assert resultado == "letra se encuentra"


def test_letra_esta_progreso():
    # Si la letra se encuentra el progreso debe cambiar.
    j = Juego("palabra")
    j.arriesgar_letra("b")
    assert j.mostrar_progreso_palabra() == "____b__"


def test_letra_esta_intentos():
    # Si la letra se encuentra el nro de intentos debe mantenerse.
    j = Juego("palabra")
    j.arriesgar_letra("b")
    assert j.intentos_disponibles() == Juego.MAX_INTENTOS


# Letra pierde
def test_letra_pierde_perdio():
    # Si arriesga maxIntentos veces y pierde perdio() debe ser True
    j = Juego("palabra")
    j.intentos_usados = Juego.MAX_INTENTOS
    j.arriesgar_letra("x")
    assert j.perdio()


def test_letra_pierde_finalizo():
    # Si arriesga maxIntentos veces y pierde finalizo() debe ser True
    j = Juego("palabra")
    j.intentos_usados = Juego.MAX_INTENTOS
    j.arriesgar_letra("x")
    assert j.finalizo()


def test_letra_pierde_mensaje():
    # Si arriesga maxIntentos veces y pierde el mensaje debe ser "letra no se encuentra"
    j = Juego("palabra")
    resultado = " "
    j.intentos_usados = Juego.MAX_INTENTOS
    resultado = j.arriesgar_letra("x")
    assert resultado == "letra no se encuentra"


def test_letra_pierde_intentos():
    # Si arriesga maxIntentos veces el nro de intentos debe ser 0.
    j = Juego("palabra")
    j.intentos_usados = Juego.MAX_INTENTOS
    j.arriesgar_letra("x")
    assert j.intentos_disponibles() == 0


def test_letra_pierde_puntaje():
    j = Juego("palabra")
    j.intentos_usados = Juego.MAX_INTENTOS
    j.arriesgar_letra("x")
    assert j.finalizo()
    assert j.puntaje() == 0


# Letra gana
def test_letra_gana_finalizo():
    # Si adivina la palabra finalizo() debe ser True
    j = Juego("celu")
    j.arriesgar_letra("c")
    j.arriesgar_letra("e")
    j.arriesgar_letra("l")
    j.arriesgar_letra("u")
    assert j.finalizo()


def test_letra_gana_mensaje():
    # Si adivina la palabra el mensaje debe ser "letra se encuentra" y acerto=True.
    j = Juego("celu")
    j.arriesgar_letra("c")
    j.arriesgar_letra("e")
    j.arriesgar_letra("l")
    resultado = ""
    resultado = j.arriesgar_letra("u")
    assert resultado == "letra se encuentra"
    assert j.acerto


def test_letra_gana_progreso():
    # Si adivina la palabra el progreso esta completo
    j = Juego("celu")
    j.arriesgar_letra("c")
    j.arriesgar_letra("e")
    j.arriesgar_letra("l")
    j.arriesgar_letra("u")
    assert j.mostrar_progreso_palabra() == "celu"


def test_letra_gana_sin_errores_puntaje():
    j = Juego("celu")
    j.arriesgar_letra("c")
    j.arriesgar_letra("e")
    j.arriesgar_letra("l")
    j.arriesgar_letra("u")
    assert j.finalizo()
    assert j.puntaje() == Juego.MAX_INTENTOS


def test_letra_gana_un_error_puntaje():
    j = Juego("celu")
    j.arriesgar_letra("x")
    j.arriesgar_letra("c")
    j.arriesgar_letra("e")
    j.arriesgar_letra("l")
    j.arriesgar_letra("u")
    assert j.finalizo()
    assert j.puntaje() == Juego.MAX_INTENTOS - 1


def test_letra_gana_dos_errores_puntaje():
    j = Juego("celu")
    j.arriesgar_letra("x")
    j.arriesgar_letra("c")
    j.arriesgar_letra("e")
    j.arriesgar_letra("y")
    j.arriesgar_letra("l")
    j.arriesgar_letra("u")
    assert j.finalizo()
    assert j.puntaje() == Juego.MAX_INTENTOS - 2


def test_letra_gana_ultimo_intento_puntaje():
    j = Juego("celu")
    j.intentos_usados = Juego.MAX_INTENTOS - 1
    j.arriesgar_letra("c")
    j.arriesgar_letra("e")
    j.arriesgar_letra("l")
    j.arriesgar_letra("u")
    assert j.finalizo()
    assert j.puntaje() == 1


# Letras usadas
def test_letras_usadas():
    j = Juego("palabra")
    j.arriesgar_letra("a")
    j.arriesgar_letra("b")
    j.arriesgar_letra("c")
    j.arriesgar_letra("d")
    j.arriesgar_letra("e")
    j.arriesgar_letra("l")
    assert j.letras_usadas == ["a", "b", "c", "d", "e", "l"]


# Juego en curso
def test_letra_juego_en_curso_finalizo():
    j = Juego("hola")
    j.arriesgar_letra("e")
    j.arriesgar_letra("a")
    assert not j.finalizo()


def test_letra_juego_en_curso_puntaje():
    j = Juego("hola")
    j.arriesgar_letra("e")
    j.arriesgar_letra("a")
    assert j.puntaje() == 0
