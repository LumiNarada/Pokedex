from Json import DataFrame
from Estadisticas import estadisticas
from Pelea import explorar, desafiar

class FueraDeRango(Exception):
    def __init__(self):
        super().__init__(self)

def lanzExcep(numero, lim1, lim2):
    if(numero< lim1 or numero > lim2):
        raise FueraDeRango()
    else:
        pass

def menu(lista,inst,lim1, lim3):
    while (True):
        try: 
            print(lista)
            opcion = int(input(inst))
            lanzExcep(opcion, lim1, lim3)
            break
        except FueraDeRango:
            print("\n¡Caramba!¡Creo que estás un poco confundido!\n")
        except ValueError:
            print("\n¡Caramba!¡Creo que estás un poco confundido!\n")
        finally:
            pass
    return opcion


class Pokemon():
    def __init__(self,nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre

pokedex=DataFrame("Pokedex")
pokemones=DataFrame("Pokemon")

"""df2.set_index('Nombre', inplace=True)"""



if (pokemones.df.loc[0, ["Nombre"][0]]=="Ninguno"):
    print("¡Hola!\n¡Este es el mundo de los pokemon!\n¡Me llamo Oak!\n¡Pero la gente me llama Profesor Pokemon!")
    print("¡Aquí hay tres pokemon!\n¡Cuando yo era joven era un buen entrenador pokemon!")
    print("Pero ahora solo me quedan tres...\n¡Te dare uno! ¿Cuál quieres?")
    p=menu(
        "1. BULBASAUR\n2. SQUIRTLE\n3. CHARMANDER",
        "Escribe el número asociado al pokemon que te gusta más ",
        1, 3)
    print("¿Te gustaría darle un nombre especial?")
    n=menu(
        "1.Si\t2. No",
        "Escribe el número asociado tu respuesta", 
        1, 2)
    if (n==1):
        n=2
        while (n==2):
            nom=input("¿Como te gustaría llamarle?")
            print("¿Estás seguro de que quieres llamarle"+str(nom)+"?")
            n=menu(
                "1.Si\t2. No",
                "Escribe el número asociado tu respuesta", 
                1, 2)
    print("¡Perfecto!")
    if (p==1):
        pokedex.capturado(1)
        elegido="Bulbasaur"
    elif (p==2):
        pokedex.capturado(4)
        elegido="Squirtle"
    elif (p==3):
        pokedex.capturado(7)
        elegido="Charmander"
    pokemones.actualizar(0, "Especie", elegido)
    if (n==1):
        pokemones.actualizar(0, "Nombre", nom)
    elif (n==2):
        pokemones.actualizar(0, "Nombre", elegido)
    pokedex.exportar()
    pokemones.exportar()
else:
    print("Tu pokemon es "+str(pokemones.df["Nombre"][0][0])+" de especie "+str(pokemones.df["Especie"][0][0]))
    estadisticas("Aver")
    explorar("Aver")
    desafiar("Aver")

