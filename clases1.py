class Moto:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color  = color
        self.__kilometraje = 0

    def info(self):
        print("{} de color {}".format(self.nombre, self.color))

    def manejar(self):
        print("Manejando...")
        self.__actualizar()

    def saludo(self):
        print("Saludando...")

    def __actualizar(self):
        self.__kilometraje += 1
        print("Actualizando kilometraje = {}km...".format(self.__kilometraje))

class CuatriMoto(Moto):
    def __init__(self, altura):
        self.altura = altura
        super().__init__("Suzuki", "rojo")

suzuki_cuatrimoto = CuatriMoto(2)
suzuki_cuatrimoto.saludo()
suzuki_cuatrimoto.info()
suzuki_cuatrimoto.manejar()