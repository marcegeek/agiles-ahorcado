import os
class Juego:
    # configuracion
    maxIntentos = 6
    intentosLetra = 1
    intentosPalabra = 2

    # Se inicializa el juego con una palabra.
    def __init__(self, palabra=None, data=None):
        if data:
            self.__dict__.update(data)
        else:
            if not palabra.replace(' ', '').isalpha():
                raise ValueError("Palabra invalida: debe contener solo letras o espacios")
            self.palabra = palabra.lower()
            self.acerto = False
            self.intentosUsados = 0
            self.letrasUsadas = []

    # Dada una letra, devuelve 4 posibles valores. (letra ya usada, letra se encuentra, letra no se encuetra, letra invalida).
    def arriesgarLetra(self, letra):
        if letra.isalpha() and len(letra) == 1:
            letra = letra.lower()
            if letra in self.letrasUsadas:
                return "letra ya usada"
            self.letrasUsadas.append(letra)
            if letra in self.palabra:
                if '_' not in self.mostrarProgresoPalabra():
                    self.acerto = True
                return "letra se encuentra"
            else:
                self.intentosUsados += self.intentosLetra
                return "letra no se encuentra"
        else:
            return "letra invalida"

    # Dada una palabra, devuelve 2 posibles valores. (palabra correcta/palabra incorrecta).
    def arriesgarPalabra(self, palabra):
        if palabra.lower() == self.palabra:
            for i in palabra:
                self.letrasUsadas.append(i)
            self.acerto = True
            return "palabra correcta"
        self.intentosUsados += self.intentosPalabra
        return "palabra incorrecta"

    # Retorna los intentos disponibles.
    def intentosDisponibles(self):
        return max(self.maxIntentos - self.intentosUsados, 0)
    
    # Retorna el progreso de la palabra.
    def mostrarProgresoPalabra(self):
        avance = ''
        for i in self.palabra:
            if i in self.letrasUsadas:
                avance = avance + i
            elif i == ' ':
                avance = avance + ' '
            else:
                avance = avance + '_'      
        return avance

    def informacionJuego(self):
        return {
            "intentos_restantes": self.intentosDisponibles(),
            "letras_usadas": ' '.join(self.letrasUsadas),
            "progreso_palabra": self.mostrarProgresoPalabra(),
            "acerto": self.acerto
        }
    
    def to_dict(self):
        return self.__dict__.copy()
