#Importación de paquetes
from DataFrames import DataFrame
from Pokemones import Pokemon
from Exepciones import menu
from Peleas import pelea, contra, pokebola, desafio, explorar
from Inicio import inicio
from Pokedex import pokedexx
from random import randint

#importación de Data Frames
pokedex=DataFrame("Pokedex")
pokemones=DataFrame("Pokemon")
ataques=DataFrame("Ataques")
npc=DataFrame("NPC")

"""df2.set_index('Nombre', inplace=True)"""
#Si no tienes ningún pokemón, o sea, si la partida es nueva, Oak te da tu nuevo pokemon
if (pokemones.df.loc[0, ["nombre"][0]]=="Ninguno"):
    inicio(pokedex, pokemones, ataques)
#Menú de acciones, puedes ver la pokedex, tus porpios pokemones o pelear con un rival o en la naturaleza 
opcion=1
while(opcion!=5):
    #La función menú es muy recurrente, tiene programadas expeciones para evitar que el usaurio haga cosas raras
    opcion=menu(
            "\n1.Ver Pokedex\n2.Inventario Pokemon\n3.Combate con un rival\n4.Explora y ecuentra un pokemon nuevo\n5.Guardar y Salir",
            "\nEscribe el número asociado tu respuesta: ", 
            1, 5)
    #Ver tu pokedex
    if(opcion==1):
        pokedexx(pokedex, pokemones, ataques)

    #Ver tus pokemones
    elif(opcion==2):
        print("algo")

    #Pelear con un rival    
    elif(opcion==3):
        pokemones=DataFrame("Pokemon")
        opcion=menu(
            "\n1. Bruck\n2. Misty",
            "\nEscribe el número asociado al entrenador que quieres desafiar: ", 
            1, 2)
        opcion-=1
        print("\n"+str(npc.df.iloc[opcion, 3]))
        rival=Pokemon(pokedex.encontrarEspecie(npc.df.iloc[opcion, 1]), pokedex.encontrarEspecie(npc.df.iloc[opcion, 1]),npc.df.iloc[opcion, 2],pokedex,pokemones, ataques)
        print("El rival ha liberado a "+str(rival.nombre))
        print("\n¿Qué pokemon usaras?")
        numero=pokemones.filas
        while (numero>=0):
            print(str(numero+1)+". "+str(pokemones.df.iloc[numero,0]))
            numero-=1
        elegido=menu(
            "",
            "Escribe el número asociado al pokemon que deseas usar: ", 
            1, pokemones.filas+1)
        elegido-=1
        elegido=Pokemon(pokemones.df.iloc[elegido,0],pokemones.df.iloc[elegido,1],pokemones.df.iloc[elegido,3],pokedex,pokemones, ataques)
        print("Has elegido a "+str(elegido.nombre))
        while(rival.vidaActual > 0 and elegido.vidaActual > 0):
            desafio(elegido, rival, ataques)
        if(elegido.vidaActual<=0):
            print("oh no, u are dead")
        else:
            print("¡El rival se ha quedado sin fuerzas!\n¡Has ganado!")
        elegido.vidaActual = pokedex.df.set_index("nombre").loc[elegido.especie, "vida_total"]

    #Buscar otros pokemons en la naturaleza  
    elif(opcion==4):
        pokemones=DataFrame("Pokemon")
        nPokedex=explorar(pokedex)
        print("\nHa aparecido un " + str(pokedex.df.set_index("num").loc[nPokedex,"nombre"]) + " salvaje")
        print("\n¿Qué pokemon seberías usar?")
        numero=pokemones.filas
        n=0
        while (n<=numero):
            print(str(n+1)+". "+str(pokemones.df.iloc[n,0]))
            n+=1
        elegido=menu(
            "",
            "Escribe el número asociado al pokemon que deseas usar: ", 
            1, pokemones.filas+1)
        elegido-=1
        elegido=Pokemon(pokemones.df.iloc[elegido,0],pokemones.df.iloc[elegido,1],pokemones.df.iloc[elegido,3],pokedex,pokemones, ataques)
        print("¡Has elegido a "+str(elegido.nombre) + "!")
        salvaje=Pokemon(pokedex.df.set_index("num").loc[nPokedex,"nombre"],pokedex.df.set_index("num").loc[nPokedex,"nombre"],elegido.lvl-3,pokedex, pokemones,ataques)
        print()
        while(salvaje.vidaActual > 0 and elegido.vidaActual > 0):
            accion=menu(
            "¿Quieres pelear o intentar capturarlo?\n1. Pelear\t2. Capturar",
            "\nEscribe el número asociado a la acción que deseas realizar ", 
            1, 2)
            if(accion==1):
                pelea(elegido, salvaje, ataques)
                if(salvaje.vidaActual>=0):
                    print(elegido.lvl, salvaje.lvl)
                    contra(elegido, salvaje, ataques)
                    if(elegido.vidaActual<=0):
                        print("oh no, u are dead")
                else:
                    print("¡El pokemon salvaje se ha quedado sin fuerzas!\n¡Has ganado!")
            else:
                pokebola(elegido, salvaje, ataques, pokedex, pokemones)
        salvaje.vidaActual = pokedex.df.set_index("nombre").loc[salvaje.especie, "vida_total"]
        elegido.vidaActual = pokedex.df.set_index("nombre").loc[elegido.especie, "vida_total"]
        pokedex.exportar()
        pokemones.exportar()
    #Salir y guardar tus datos
    elif(opcion==5):
        pokedex.exportar()
        pokemones.exportar()
        print("¡¡¡Adios!!!")



