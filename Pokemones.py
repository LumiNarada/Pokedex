import pandas as pd
class Pokemon():
    def __init__(self,nombre,especie,pokedex):
        self._nombre = nombre
        self._especie = especie
        self._num=pokedex.df.set_index("nombre").loc[self._especie, "num"]
        self._tipo=pokedex.df.set_index("nombre").loc[self._especie, "tipo"]
        self._descripcion=pokedex.df.set_index("nombre").loc[self._especie, "tipo"]
    @property
    def num(self):
        return self._num
    @property
    def nombre(self):
        return self._nombre
    @property
    def especie(self):
        return self._especie
    @property
    def tipo(self):
        return self._tipo
    @property
    def descripcion(self):
        return self._descripcion
    

    def capturar(self, pokedex, pokemones, lvl):
        pokemon= pd.DataFrame({
            "nombre":[self._nombre],
            "especie":[self._especie],
            "vida_actual":[pokedex.df.set_index("nombre").loc[self._especie, "vida_total"]],
            "lvl_actual":[lvl],
            "exp_actual":[0],
            "evol":[0],
            "a_1":["Ninguno"],
            "a_2":["Ninguno"],
            "a_3":["Ninguno"],
            "a_4":["Ninguno"]
        })
        pokemones.concatenar(pokemon)