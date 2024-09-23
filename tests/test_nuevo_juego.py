from ahorcado import Juego


# Reiniciar juego
def test_reiniciar_juego():
    # Si se reinicia el juego la palabra debe cambiar.
    j = Juego("hola")
    j.arriesgar_letra("h")
    j.__init__("nuevo")
    assert j.palabra == "nuevo"


def test_reiniciar_juego_intentos():
    # Si se reinicia el juego intentos usados debe ser 0.
    j = Juego("hola")
    j.arriesgar_letra("h")
    j.__init__("hola")
    assert j.intentos_disponibles() == Juego.MAX_INTENTOS


def test_reiniciar_juego_letras_usadas():
    # Si se reinicia el juego letras usadas debe estar vacio.
    j = Juego("hola")
    j.arriesgar_letra("h")
    j.__init__("hola")
    assert j.letras_usadas == []


def test_reiniciar_juego_progreso():
    # Si se reinicia el juego el progreso debe estar vacio.
    j = Juego("hola")
    j.arriesgar_letra("h")
    j.__init__("hola")
    assert j.mostrar_progreso_palabra() == "____"
