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
        
    def iniciarJuego(self):
        while(self.intentosDisponibles() > 0):
            self.informacionPartida()
            print("Ingrese letra o palabra a arriesgar")
            i = input()
            
            if len(i) == 1:
                resultado = self.arriesgarLetra(i)
                print(resultado.upper())
                if resultado == "ganaste":
                    break
            else:
                resultado = self.arriesgarPalabra(i)
                print(resultado.upper())
                if resultado == "ganaste":
                    break
        
    def informacionPartida(self):
        print("Intentos restantes: ", self.intentosDisponibles())
        print("Letras usadas: ", ' '.join(self.letrasUsadas))
        print(self.mostrarProgresoPalabra())

    def arriesgarLetra(self, letra):
        if letra.isalpha() and len(letra) == 1:
            letra = letra.lower()
            if letra in self.letrasUsadas:
                return "letra ya usada"
            self.letrasUsadas.append(letra)
            if letra in self.palabra:
                if '_' not in self.mostrarProgresoPalabra():
                    self.acerto = True
                    return "ganaste"
                return "letra se encuentra"
            else:
                if self.intentosDisponibles()<=0:
                    return "pierde"
                else:
                    self.intentosUsados += self.intentosLetra
                    return "letra no se encuentra"
        else:
            return "letra invalida"

    def arriesgarPalabra(self, palabra):
        if palabra.lower() == self.palabra:
            for i in palabra:
                self.letrasUsadas.append(i)
            return "ganaste"
        self.intentosUsados += self.intentosPalabra
        if self.intentosDisponibles() == 0:
            return "perdiste"
        else:
            return "palabra incorrecta"

    def intentosDisponibles(self):
        return max(self.maxIntentos - self.intentosUsados, 0)
    
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




j = Juego("nacho")

j.iniciarJuego()