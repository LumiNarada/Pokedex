from Json import importar, exportar
from Estadisticas import estadisticas
from Pelea import explorar, desafiar

class Pokemon():
    def __init__(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre

pikachu = Pokemon("Pikachu")
importar()
exportar()
estadisticas()
explorar()
desafiar()
