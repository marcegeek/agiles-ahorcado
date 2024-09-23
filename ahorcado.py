"""Lógica del juego del ahorcado.

La clase Juego implementa la lógica de un único juego, mientras que la clase Partida
implementa la lógica de una partida entre dos jugadores con 6 rondas intercaladas para cada uno.
"""

from __future__ import annotations


class Juego:
    """Lógica básica del juego del ahorcado."""

    # constantes de la clase
    MAX_INTENTOS = 6
    INTENTOS_LETRA = 1
    INTENTOS_PALABRA = 2

    def __init__(self, palabra: str | None = None, data: dict | None = None) -> None:
        """Inicializa el juego con una palabra."""
        if data:
            self.__dict__.update(data)
        else:
            if not palabra.replace(" ", "").isalpha():
                error = "Palabra invalida: debe contener solo letras o espacios"
                raise ValueError(error)
            self.palabra = palabra.lower()
            self.acerto = False
            self.intentos_usados = 0
            self.letras_usadas = []

    def arriesgar_letra(self, letra: str) -> str:
        """Arriesga una letra.

        Dada una letra, devuelve uno de 4 valores posibles:
        "letra ya usada, "letra se encuentra", "letra no se encuentra", "letra invalida"
        """
        if letra.isalpha() and len(letra) == 1:
            letra = letra.lower()
            if letra in self.letras_usadas:
                return "letra ya usada"
            self.letras_usadas.append(letra)
            if letra in self.palabra:
                if "_" not in self.mostrar_progreso_palabra():
                    self.acerto = True
                return "letra se encuentra"
            self.intentos_usados += self.INTENTOS_LETRA
            return "letra no se encuentra"
        return "letra invalida"

    def arriesgar_palabra(self, palabra: str) -> str:
        """Arriesga una palabra.

        Dada una palabra, devuelve uno de 2 valores posibles:
        "palabra correcta", "palabra incorrecta"
        """
        if palabra.lower() == self.palabra:
            for i in palabra:
                self.letras_usadas.append(i)
            self.acerto = True
            return "palabra correcta"
        self.intentos_usados += self.INTENTOS_PALABRA
        return "palabra incorrecta"

    def intentos_disponibles(self) -> int:
        """Retorna los intentos disponibles."""
        return max(self.MAX_INTENTOS - self.intentos_usados, 0)

    def mostrar_progreso_palabra(self) -> str:
        """Retorna el progreso de la palabra."""
        avance = ""
        for i in self.palabra:
            if i in self.letras_usadas:
                avance = avance + i
            elif i == " ":
                avance = avance + " "
            else:
                avance = avance + "_"
        return avance

    def perdio(self) -> bool:
        """Retorna si se perdió el juego (implica que está finalizado)."""
        return not self.acerto and self.intentos_disponibles() == 0

    def finalizo(self) -> bool:
        """Retorna si el juego finalizó."""
        return self.acerto or self.perdio()

    def puntaje(self) -> int:
        """Retorna el puntaje del juego."""
        return 0 if not self.acerto else self.intentos_disponibles()

    def to_dict(self) -> dict:
        """Retorna el juego serializado en un diccionario."""
        return self.__dict__.copy()


class Partida:
    """Lógica de una partida a 6 rondas entre dos jugadores."""

    # constantes de la clase
    NUM_RONDAS = 6  # rondas por cada jugador

    def __init__(self, data: dict | None = None) -> None:
        """Inicializa la partida."""
        if data:
            self.__dict__.update(data)
            if self.juego:
                self.juego = Juego(data=self.juego)
        else:
            self.rondas = [0, 0]
            self.id_jugador_actual = None
            self.juego = None
            self.puntos = [0, 0]

    def comenzar_ronda(self, palabra: str) -> None:
        """Comienza una nueva ronda con la palabra a adivinar."""
        if not self.id_jugador_actual:
            self.id_jugador_actual = 1
        else:
            self.id_jugador_actual = 0
        self.rondas[self.id_jugador_actual] += 1
        self.juego = Juego(palabra)

    def actualizar_puntos(self) -> None:
        """Actualiza los puntos del jugador actual."""
        if self.juego.acerto:
            self.puntos[self.id_jugador_actual] += self.juego.puntaje()

    def ronda_finalizo(self) -> bool:
        """Retorna si finalizó la ronda actual."""
        return self.juego is not None and self.juego.finalizo()

    def finalizo(self) -> bool:
        """Retorna si finalizó la partida."""
        return self.ronda_finalizo() and self.rondas[0] == self.NUM_RONDAS

    def puntos_jugador(self, id_jugador: int) -> int:
        """Retorna los puntos del jugador indicado."""
        return self.puntos[id_jugador]

    def to_dict(self) -> dict:
        """Retorna la partida serializada en un diccionario."""
        d = self.__dict__.copy()
        if d["juego"]:
            d["juego"] = d["juego"].to_dict()
        return d
