from Exepciones import menu
from Pokemones import Pokemon
def pokedexx(pokedex, pokemones, ataques):
    print("\nHas descubierto "+str(pokedex.df['captura'].value_counts()[1])+" pokemon")
    print("Aun hay "+str(pokedex.df['captura'].value_counts()[0])+" pokemon por descubrir\n")
    print("Pokemones descubiertos: \n")
    count=0
    while(pokedex.filas>=count):
        if(pokedex.df.iloc[count,[7]][0]==1):
            print (str(pokedex.df.iloc[count,[0]][0])+". "+str(pokedex.df.iloc[count,[1]][0]))
        count+=1
    while(True):
        try:
            info=1
            while(info!=0):
                info=menu(
                    "\n¿Deseas ver la información de algun pokemon?\n(Si no quieres ver la información de ningún pokemon, escribe 0)",
                    "\nEscribe el número asociado tu respuesta: ", 
                    0, 150)
                if (info!=0):
                    if (pokedex.df.set_index("nombre").loc[pokedex.encontrarEspecie(info), "captura"]==1):
                        print("\nN°: "+str(pokedex.df.set_index("nombre").loc[pokedex.encontrarEspecie(info), "num"]))
                        print("Nombre: "+str(pokedex.encontrarEspecie(info)))
                        print("Tipo: "+str(pokedex.df.set_index("nombre").loc[pokedex.encontrarEspecie(info), "tipo"]))
                        print("Descripción: \""+str(pokedex.df.set_index("nombre").loc[pokedex.encontrarEspecie(info), "descripcion"]) + "\" ")
                    else:
                        print("Información insuficiente, aun no has descubierto ese pokemon")
            break
        except IndexError:
            print("Información insuficiente, no hay registros de ese pokemon")
        except KeyError:
            print("Información insuficiente, no hay registros de ese pokemon")