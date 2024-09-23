from ahorcado import Juego


# Palabra acierta
def test_palabra_acierta_mensaje():
    # Si adivina la palabra el mensaje es "palabra correcta" y acerto=True.
    j = Juego("hola")
    resultado = j.arriesgar_palabra("hola")
    assert resultado == "palabra correcta"
    assert j.acerto


def test_palabra_acierta_finalizo():
    j = Juego("hola")
    j.arriesgar_palabra("hola")
    assert j.finalizo()


def test_palabra_acierta_progreso():
    # Si adivina la palabra el progreso esta completo.
    j = Juego("hola")
    j.arriesgar_palabra("hola")
    assert j.finalizo()
    assert j.mostrar_progreso_palabra() == "hola"


def test_palabra_acierta_sin_errores_puntaje():
    j = Juego("hola")
    j.arriesgar_palabra("hola")
    assert j.finalizo()
    assert j.puntaje() == Juego.MAX_INTENTOS


def test_palabra_acierta_un_error_puntaje():
    j = Juego("hola")
    # pierde dos intentos
    j.arriesgar_palabra("hoja")
    j.arriesgar_palabra("hola")
    assert j.finalizo()
    assert j.puntaje() == Juego.MAX_INTENTOS - 2


def test_palabra_acierta_dos_errores_puntaje():
    j = Juego("hola")
    # pierde cuatro intentos
    j.arriesgar_palabra("hoja")
    j.arriesgar_palabra("loza")
    j.arriesgar_palabra("hola")
    assert j.finalizo()
    assert j.puntaje() == Juego.MAX_INTENTOS - 4


# Palabra incorrecta
def test_palabra_incorrecta_mensaje():
    # Si arriesga palabra y es incorrecta el mensaje es "palabra incorrecta".
    j = Juego("hola")
    resultado = j.arriesgar_palabra("chau")
    assert resultado == "palabra incorrecta"


def test_palabra_incorrecta_progreso():
    # Si arriesga palabra y es incorrecta el progreso deberia mantenerse.
    j = Juego("hola")
    j.arriesgar_palabra("chau")
    assert j.mostrar_progreso_palabra() == "____"


def test_palabra_incorrecta_intentos():
    # Si arriesga palabra y los intentos disponibles deben disminuir.
    j = Juego("hola")
    j.arriesgar_palabra("chau")
    assert j.intentos_disponibles() == Juego.MAX_INTENTOS - Juego.INTENTOS_PALABRA


# Palabra pierde
def test_palabra_pierde_perdio():
    j = Juego("hola")
    j.intentos_usados = Juego.MAX_INTENTOS
    j.arriesgar_palabra("chau")
    assert j.perdio()


def test_palabra_pierde_finalizo():
    j = Juego("hola")
    j.intentos_usados = Juego.MAX_INTENTOS
    j.arriesgar_palabra("chau")
    assert j.finalizo()


def test_palabra_pierde_mensaje():
    # Si arriesga palabra y se queda sin intentos el mensaje es "palabra incorrecta".
    j = Juego("hola")
    j.intentos_usados = Juego.MAX_INTENTOS
    resultado = j.arriesgar_palabra("chau")
    assert resultado == "palabra incorrecta"


def test_palabra_pierde_intentos():
    # Si arriesga palabra y pierde los intentos disponibles son 0.
    j = Juego("hola")
    j.intentos_usados = Juego.MAX_INTENTOS
    j.arriesgar_palabra("chau")
    assert j.intentos_disponibles() == 0


def test_palabra_pierde_puntaje():
    # Si arriesga palabra y pierde los intentos disponibles son 0.
    j = Juego("hola")
    j.intentos_usados = Juego.MAX_INTENTOS
    j.arriesgar_palabra("chau")
    assert j.finalizo()
    assert j.puntaje() == 0


# Palabra con espacios.
def test_palabra_con_espacios_progreso():
    j = Juego("hola mundo")
    j.arriesgar_letra("o")
    assert j.mostrar_progreso_palabra() == "_o__ ____o"


# Juego en curso
def test_palabra_juego_en_curso_finalizo():
    j = Juego("hola")
    j.arriesgar_palabra("chau")
    assert not j.finalizo()


def test_palabra_juego_en_curso_puntaje():
    j = Juego("hola")
    j.arriesgar_palabra("chau")
    assert j.puntaje() == 0
