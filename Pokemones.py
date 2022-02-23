from numpy import NaN
import pandas as pd
import numpy as np
import random
class Pokemon():
    def __init__(self,nombre,especie,lvl,pokedex, pokemones, ataques):
        self._nombre = nombre
        self._especie = especie
        self._lvl=lvl
        self._num=pokedex.df.set_index("nombre").loc[self._especie, "num"]
        self._tipo=pokedex.df.set_index("nombre").loc[self._especie, "tipo"]
        self._descripcion=pokedex.df.set_index("nombre").loc[self._especie, "descripcion"]
        self._captura=pokedex.df.set_index("nombre").loc[self._especie, "captura"]
        
        filtrotipo= ataques.df["tipo"]==self._tipo
        filtrolvl = ataques.df["lvl_aprendizaje"] <= self._lvl

        if(pokemones.df[pokemones.df["nombre"]==self._nombre].shape[0]==1):
            self._ataqueA=pokemones.df.set_index("nombre").loc[self.nombre, "ataqueA"]
            self._ataqueB=pokemones.df.set_index("nombre").loc[self.nombre, "ataqueB"]
            self._ataqueC=pokemones.df.set_index("nombre").loc[self.nombre, "ataqueC"]
            self._ataqueD=pokemones.df.set_index("nombre").loc[self.nombre, "ataqueD"]
            self._vidaActual=pokemones.df.set_index("nombre").loc[self.nombre, "vida_actual"]
        elif(ataques.df[filtrotipo&filtrolvl].shape[0]<4):
            self._vidaActual=pokedex.df.set_index("nombre").loc[self._especie, "vida_total"]
            aprendidos=ataques.df[filtrotipo&filtrolvl].shape[0]-1
            self._ataqueD="Ninguno"
            self._ataqueC="Ninguno"
            self._ataqueB="Ninguno"
            self._ataqueA="Ninguno"

            while(aprendidos>=0):
                habilidad=ataques.df[filtrotipo&filtrolvl].iloc[aprendidos, 0]
                if(aprendidos==3):
                    self._ataqueD=habilidad
                elif(aprendidos==2):
                    self._ataqueC=habilidad
                elif(aprendidos==1):
                    self._ataqueB=habilidad
                elif(aprendidos==0):
                    self._ataqueA=habilidad
                aprendidos-=1
        else:
            self._vidaActual=pokedex.df.set_index("nombre").loc[self._especie, "vida_total"]
            aprendidos=ataques.df[filtrotipo&filtrolvl].shape[0]-1
            array=np.random.randint(1, aprendidos, size=1)
            tamaño=1
            while(tamaño<4):
                numero=random.randint(1,aprendidos)
                ok=1
                while(ok==1):
                    ok=0
                    for elemento in array:
                        if (elemento==numero):
                            numero=random.randint(1,5)
                            ok=1
                array=np.append(array, numero)
                tamaño+=1
            self._ataqueA=ataques.df[filtrotipo&filtrolvl].iloc[array[0], 0]
            self._ataqueB=ataques.df[filtrotipo&filtrolvl].iloc[array[1], 0]
            self._ataqueC=ataques.df[filtrotipo&filtrolvl].iloc[array[2], 0]
            self._ataqueD=ataques.df[filtrotipo&filtrolvl].iloc[array[3], 0]
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
    
    @property
    def vidaActual(self):
        return self._vidaActual
    
    @property
    def ataqueA(self):
        return self._ataqueA

    @property
    def ataqueB(self):
        return self._ataqueB
    
    @property
    def ataqueC(self):
        return self._ataqueC
    
    @property
    def ataqueD(self):
        return self._ataqueD

    @property
    def lvl(self):
        return self._lvl

    @property
    def captura(self):
        return self._captura

    @vidaActual.setter
    def vidaActual(self, valor):
        self._vidaActual = valor

    @lvl.setter
    def lvl(self, valor):
        self._lvl = valor
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    def capturar(self, pokedex, pokemones):
        
        pokemon= pd.DataFrame({
            "nombre":[self._nombre],
            "especie":[self._especie],
            "vida_actual":[self._vidaActual],
            "lvl_actual":[self._lvl],
            "exp_actual":[0],
            "evol":[0],
            "ataqueA":[self._ataqueA],
            "ataqueB":[self._ataqueB],
            "ataqueC":[self._ataqueC],
            "ataqueD":[self._ataqueC]
        })
        
        pokemones.concatenar(pokemon)

    def atacar(self, ataque, ataques):
        if(ataque==1):
            danio=self.ataqueA
        elif(ataque==2):
            danio=self.ataqueB
        elif(ataque==3):
            danio=self.ataqueC
        elif(ataque==4):
            danio=self.ataqueD
        filtro = ataques.df["nombre"] == danio
        danio = ataques.df[filtro].iloc[0,3]
        danio=danio*self._lvl*2
        return danio


    def recibirDaño(self, danio):
        self.vidaActual=self.vidaActual-danio