"""Lógica del juego del ahorcado.

La clase Juego implementa la lógica de un único juego, mientras que la clase Partida
implementa la lógica de una partida entre dos jugadores con 6 rondas intercaladas para cada uno.
"""

from __future__ import annotations


class Juego:
    """Lógica básica del juego del ahorcado."""

    # configuracion
    maxIntentos = 6
    intentosLetra = 1
    intentosPalabra = 2

    def __init__(self, palabra: str | None=None, data: dict | None=None) -> None:
        """Inicializa el juego con una palabra."""
        if data:
            self.__dict__.update(data)
        else:
            if not palabra.replace(" ", "").isalpha():
                raise ValueError("Palabra invalida: debe contener solo letras o espacios")
            self.palabra = palabra.lower()
            self.acerto = False
            self.intentosUsados = 0
            self.letrasUsadas = []

    def arriesgarLetra(self, letra: str) -> str:
        """Arriesga una letra.

        Dada una letra, devuelve uno de 4 valores posibles:
        "letra ya usada, "letra se encuentra", "letra no se encuentra", "letra invalida"
        """
        if letra.isalpha() and len(letra) == 1:
            letra = letra.lower()
            if letra in self.letrasUsadas:
                return "letra ya usada"
            self.letrasUsadas.append(letra)
            if letra in self.palabra:
                if "_" not in self.mostrarProgresoPalabra():
                    self.acerto = True
                return "letra se encuentra"
            else:
                self.intentosUsados += self.intentosLetra
                return "letra no se encuentra"
        else:
            return "letra invalida"

    def arriesgarPalabra(self, palabra: str) -> str:
        """Arriesga una palabra.

        Dada una palabra, devuelve uno de 2 valores posibles:
        "palabra correcta", "palabra incorrecta"
        """
        if palabra.lower() == self.palabra:
            for i in palabra:
                self.letrasUsadas.append(i)
            self.acerto = True
            return "palabra correcta"
        self.intentosUsados += self.intentosPalabra
        return "palabra incorrecta"

    def intentosDisponibles(self) -> int:
        """Retorna los intentos disponibles."""
        return max(self.maxIntentos - self.intentosUsados, 0)

    def mostrarProgresoPalabra(self) -> str:
        """Retorna el progreso de la palabra."""
        avance = ""
        for i in self.palabra:
            if i in self.letrasUsadas:
                avance = avance + i
            elif i == " ":
                avance = avance + " "
            else:
                avance = avance + "_"
        return avance

    def perdio(self) -> bool:
        """Retorna si se perdió el juego (implica que está finalizado)."""
        return not self.acerto and self.intentosDisponibles() == 0

    def finalizo(self) -> bool:
        """Retorna si el juego finalizó."""
        return self.acerto or self.perdio()

    def puntaje(self) -> int:
        """Retorna el puntaje del juego."""
        return 0 if not self.acerto else self.intentosDisponibles()

    def to_dict(self) -> dict:
        """Retorna el juego serializado en un diccionario."""
        return self.__dict__.copy()


class Partida:
    """Lógica de una partida a 6 rondas entre dos jugadores."""

    numRondas = 6  # rondas por cada jugador

    def __init__(self, data: dict | None=None) -> None:
        """Inicializa la partida."""
        if data:
            self.__dict__.update(data)
            if self.juego:
                self.juego = Juego(data=self.juego)
        else:
            self.rondas = [0, 0]
            self.idJugadorActual = None
            self.juego = None
            self.puntos = [0, 0]

    def comenzarRonda(self, palabra: str) -> None:
        """Comienza una nueva ronda con la palabra a adivinar."""
        if self.idJugadorActual is None:
            self.idJugadorActual = 1
        elif self.idJugadorActual == 0:
            self.idJugadorActual = 1
        else:
            self.idJugadorActual = 0
        self.rondas[self.idJugadorActual] += 1
        self.juego = Juego(palabra)

    def actualizarPuntos(self) -> None:
        """Actualiza los puntos del jugador actual."""
        if self.juego.acerto:
            self.puntos[self.idJugadorActual] += self.juego.puntaje()

    def rondaFinalizo(self) -> bool:
        """Retorna si finalizó la ronda actual."""
        return self.juego is not None and self.juego.finalizo()

    def finalizo(self) -> bool:
        """Retorna si finalizó la partida."""
        return self.rondaFinalizo() and self.rondas[0] == self.numRondas

    def puntosJugador(self, idJugador: int) -> int:
        """Retorna los puntos del jugador indicado."""
        return self.puntos[idJugador]

    def to_dict(self) -> dict:
        """Retorna la partida serializada en un diccionario."""
        d = self.__dict__.copy()
        if d["juego"]:
            d["juego"] = d["juego"].to_dict()
        return d
