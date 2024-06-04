class Juego:
    MAX_INTENTOS = 6
    INTENTOS_LETRA = 1
    INTENTOS_PALABRA = 2

    def __init__(self, palabra):
        self.palabra = palabra.lower()
        self.acerto = False
        self.intentos_usados = 0
        self.letras_adivinadas = set()

    def arriesgar_letra(self, letra):
        if letra.isalpha() and len(letra) == 1:
            letra = letra.lower()
            if letra in self.letras_adivinadas:
                return "letra ya usada"
            self.letras_adivinadas.add(letra)
            if letra in self.palabra:
                return "letra se encuentra"
            else:
                return "letra no se encuentra"
        else:
            return "letra invalida"

    def arriesgar_palabra(self, palabra):
        if self.intentos_disponibles() == 0:
            raise Exception('Intentos agotados')
        self.intentos_usados += self.INTENTOS_PALABRA
        if palabra.lower() == self.palabra:
           self.acerto = True

    def intentos_disponibles(self):
        return max(self.MAX_INTENTOS - self.intentos_usados, 0)

    def acierta(self):
        return self.acerto

    def pierde(self):
        return self.intentos_usados() == 0 and not self.acierta()
