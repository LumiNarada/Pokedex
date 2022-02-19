from Json import DataFrame
from Estadisticas import estadisticas
from Pelea import explorar, desafiar

class Pokemon():
    def __init__(self,nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre

pikachu = Pokemon("Pikachu")
pikachu.getNombre()
pokedex=DataFrame("Pokedex")
print(pokedex.df["nombre"][1])
pokedex.capturado(1)
pokedex.exportar()



estadisticas("Aver")
explorar("Aver")
desafiar("Aver")

