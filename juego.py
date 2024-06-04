class Juego:

    def __init__(self, palabra):
        self.palabra = palabra.lower()
        self.acerto = False

    def arriesgar_letra(self, letra):
        pass

    def arriesgar_palabra(self, palabra):
        if palabra.lower() == self.palabra:
           self.acerto = True

    def intentos_disponibles(self):
        pass

    def acierta(self):
        return self.acerto

    def pierde(self):
        pass
