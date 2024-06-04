class Juego:
    # configuracion
    maxIntentos = 6
    intentosLetra = 1
    intentosPalabra = 2

    # inicializar el juego con una palabra
    def __init__(self, palabra):
        self.palabra = palabra.lower()
        self.acerto = False
        self.intentosUsados = 0
        self.letrasUsadas = []
        
    def informacionPartida(self):
        print("Intentos restantes: ", (self.maxIntentos-self.intentosUsados) )
        
        print("Letras usadas: ")
        for i in self.letrasUsadas:
            print(i)

    def arriesgarLetra(self, letra):
        if letra.isalpha() and len(letra) == 1:
            letra = letra.lower()
            if letra in self.letrasUsadas:
                return "letra ya usada"
            self.letrasUsadas.append(letra)
            if letra in self.palabra:
                return "letra se encuentra"
            else:
                self.intentosUsados += self.intentosLetra
                return "letra no se encuentra"
        else:
            return "letra invalida"

    def arriesgarPalabra(self, palabra):
        if self.intentosDisponibles() == 0:
            return "perdiste"
        self.intentosUsados += self.intentosPalabra
        if palabra.lower() == self.palabra:
            return "ganaste"

    def intentosDisponibles(self):
        return max(self.maxIntentos - self.intentosUsados, 0)

