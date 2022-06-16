class Mascota:
    def __init__(self):
        print("Animal doméstico")
    def ladrar(self):
        print("No toda mascota puede ladrar")

class Perro(Mascota):
    def ladrar(self):
        print("Un perro puede ladrar")

class Gato(Mascota):
    def ladrar(self):
        print("Un gato no puede ladrar")

fido = Perro()
fido.ladrar()

michi = Gato()
michi.ladrar()