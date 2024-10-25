"""Lógica del juego del ahorcado.

La clase Juego implementa la lógica de un único juego, mientras que la clase Partida
implementa la lógica de una partida entre dos jugadores con 6 rondas intercaladas para cada uno.
"""

from __future__ import annotations

from typing import Any


class AhorcadoError(Exception):
    """Clase custom para errores del juego del ahorcado."""

    def __init__(self, mensaje: str) -> None:
        """Inicializa la excepción con un mensaje."""
        super().__init__(mensaje)


class Juego:
    """Lógica básica del juego del ahorcado."""

    # constantes de la clase
    MAX_INTENTOS = 6
    INTENTOS_LETRA = 1
    INTENTOS_PALABRA = 2

    def __init__(
        self,
        palabra: str,
        acerto: bool | None = None,
        intentos_usados: int | None = None,
        letras_usadas: list[str] | None = None,
    ) -> None:
        """Inicializa el juego con una palabra."""
        if not palabra.replace(" ", "").isalpha():
            error = "Palabra invalida: debe contener solo letras o espacios"
            raise AhorcadoError(error)
        self.palabra = palabra.lower()
        self.acerto = acerto if acerto is not None else False
        self.intentos_usados = intentos_usados if intentos_usados is not None else 0
        self._letras_usadas = set(letras_usadas) if letras_usadas is not None else set()

    def arriesgar_letra(self, letra: str) -> str:
        """Arriesga una letra.

        Dada una letra, devuelve uno de 4 valores posibles:
        "letra ya usada, "letra se encuentra", "letra no se encuentra", "letra invalida"
        """
        if letra.isalpha() and len(letra) == 1:
            letra = letra.lower()
            if letra in self._letras_usadas:
                return "letra ya usada"
            self._letras_usadas.add(letra)
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
        palabra = palabra.lower()
        if palabra == self.palabra:
            self._letras_usadas.update(palabra)
            self.acerto = True
            return "palabra correcta"
        self.intentos_usados += self.INTENTOS_PALABRA
        return "palabra incorrecta"

    def intentos_disponibles(self) -> int:
        """Retorna los intentos disponibles."""
        return max(self.MAX_INTENTOS - self.intentos_usados, 0)

    @property
    def letras_usadas(self) -> list[str]:
        """Devuelve las letras usadas, ordenadas y sin repeticiones."""
        return sorted(self._letras_usadas)

    def mostrar_progreso_palabra(self) -> str:
        """Retorna el progreso de la palabra."""
        avance = ""
        for i in self.palabra:
            if i in self._letras_usadas:
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

    def to_dict(self) -> dict[str, Any]:
        """Retorna el juego serializado en un diccionario."""
        return {
            "palabra": self.palabra,
            "acerto": self.acerto,
            "intentos_usados": self.intentos_usados,
            "letras_usadas": self.letras_usadas,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Juego:
        """Crea un juego a partir de los datos serializados."""
        palabra = data["palabra"]
        acerto = data["acerto"]
        intentos_usados = data["intentos_usados"]
        letras_usadas = data["letras_usadas"]
        return cls(palabra, acerto=acerto, intentos_usados=intentos_usados, letras_usadas=letras_usadas)


class Partida:
    """Lógica de una partida a 6 rondas entre dos jugadores."""

    # constantes de la clase
    NUM_RONDAS = 6  # rondas por cada jugador

    def __init__(
        self,
        rondas: list[int] | None = None,
        id_jugador_actual: int | None = None,
        juego: Juego | None = None,
        puntos: list[int] | None = None,
        puntos_actualizados: bool | None = None,
    ) -> None:
        """Inicializa la partida."""
        self.rondas = rondas if rondas is not None else [0, 0]
        self.id_jugador_actual = id_jugador_actual
        self.juego = juego
        self.puntos = puntos if puntos is not None else [0, 0]
        self.puntos_actualizados = bool(puntos_actualizados)

    def comenzar_ronda(self, palabra: str) -> None:
        """Comienza una nueva ronda con la palabra a adivinar."""
        if not self.id_jugador_actual:
            self.id_jugador_actual = 1
        else:
            self.id_jugador_actual = 0
        self.rondas[self.id_jugador_actual] += 1
        self.juego = Juego(palabra)
        self.puntos_actualizados = False

    def actualizar_puntos(self) -> None:
        """Actualiza los puntos del jugador actual."""
        if self.puntos_actualizados:
            return
        if not self.juego or self.id_jugador_actual is None:
            error = "No se puede actualizar puntos si no se inició ninguna ronda"
            raise AhorcadoError(error)
        if self.juego.acerto:
            self.puntos[self.id_jugador_actual] += self.juego.puntaje()
            self.puntos_actualizados = True

    def ronda_finalizo(self) -> bool:
        """Retorna si finalizó la ronda actual."""
        return self.juego is not None and self.juego.finalizo()

    def finalizo(self) -> bool:
        """Retorna si finalizó la partida."""
        return self.ronda_finalizo() and self.rondas[0] == self.NUM_RONDAS

    def puntos_jugador(self, id_jugador: int) -> int:
        """Retorna los puntos del jugador indicado."""
        return self.puntos[id_jugador]

    def ganador(self) -> int | None:
        """Obtiene el id del ganador.

        Devuelve None si la partida aun no finalizó o -1 si hay empate.
        """
        if self.puntos[0] > self.puntos[1]:
            return 0
        elif self.puntos[0] < self.puntos[1]:
            return 1
        return -1

    def empate(self) -> bool | None:
        """Retorna si hay empate or None si la partida aun no finalizó."""
        return self.ganador() == -1

    def to_dict(self) -> dict[str, Any]:
        """Retorna la partida serializada en un diccionario."""
        return {
            "rondas": self.rondas,
            "id_jugador_actual": self.id_jugador_actual,
            "juego": self.juego.to_dict() if self.juego else None,
            "puntos": self.puntos,
            "puntos_actualizados": self.puntos_actualizados,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Partida:
        """Crea una partida a partir de los datos serializados."""
        rondas = data["rondas"]
        id_jugador_actual = data["id_jugador_actual"]
        juego = Juego.from_dict(data["juego"]) if data["juego"] else None
        puntos = data["puntos"]
        puntos_actualizados = data["puntos_actualizados"]
        return cls(
            rondas=rondas,
            id_jugador_actual=id_jugador_actual,
            juego=juego,
            puntos=puntos,
            puntos_actualizados=puntos_actualizados,
        )
