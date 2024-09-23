from ahorcado import Juego


# Inicializar juego
def test_inicializar_juego_palabra_vacia():
    try:
        Juego("")
    except ValueError as e:
        assert str(e) == "Palabra invalida: debe contener solo letras o espacios"


def test_inicializar_juego_palabra_con_numeros():
    try:
        Juego("palabra123")
    except ValueError as e:
        assert str(e) == "Palabra invalida: debe contener solo letras o espacios"


def test_inicializar_juego_palabra_con_simbolos():
    try:
        Juego("pal@bra")
    except ValueError as e:
        assert str(e) == "Palabra invalida: debe contener solo letras o espacios"


def test_inicializar_juego_palabra_con_mezcla_de_caracteres():
    try:
        Juego("palabra123 con espacios")
    except ValueError as e:
        assert str(e) == "Palabra invalida: debe contener solo letras o espacios"


def test_inicializacion_juego_progreso():
    j = Juego("palabra")
    assert j.mostrar_progreso_palabra() == "_______"


def test_inicializacion_juego_intentos():
    j = Juego("palabra")
    assert j.intentos_disponibles() == Juego.MAX_INTENTOS


def test_inicializacion_juego_letras_usadas():
    j = Juego("palabra")
    assert j.letras_usadas == []


def test_inicializacion_juego_bool_acerto():
    j = Juego("palabra")
    assert not j.acerto


def test_inicializacion_juego_puntaje():
    j = Juego("palabra")
    assert j.puntaje() == 0


def test_inicializacion_juego_data_intentos(juego_data):
    j = juego_data("palabra")
    assert j.intentos_disponibles() == Juego.MAX_INTENTOS


def test_inicializacion_juego_data_letras_usadas(juego_data):
    j = juego_data("palabra")
    assert j.letras_usadas == []
