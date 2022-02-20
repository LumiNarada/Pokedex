from Json import DataFrame
from Pokemones import Pokemon
from Estadisticas import estadisticas
from Pelea import explorar, desafiar
from Exepciones import menu
import pandas as pd
pokedex=DataFrame("Pokedex")
pokemones=DataFrame("Pokemon")

"""df2.set_index('Nombre', inplace=True)"""

if (pokemones.df.loc[0, ["nombre"][0]]=="Ninguno"):
    print("\n¡Hola!\n¡Este es el mundo de los pokemon!\n¡Me llamo Oak!\n¡Pero la gente me llama Profesor Pokemon!")
    print("¡Aquí hay tres pokemon!\n¡Cuando yo era joven era un buen entrenador pokemon!")
    print("Pero ahora solo me quedan tres...\n \n¡Te dare uno! ¿Cuál quieres?\n")
    p=menu(
        "1. BULBASAUR\t2. CHARMANDER\t3. SQUIRTLE",
        "Escribe el número asociado al pokemon que te gusta más: ",
        1, 3)
    print("\n¿Te gustaría darle un nombre especial?")
    n=menu(
        "1.Si\t2. No\n",
        "Escribe el número asociado tu respuesta: ", 
        1, 2)
    if (n==1):
        n=2
        while (n==2):
            nom=input("¿Como te gustaría llamarle?")
            print("¿Estás seguro de que quieres llamarle "+str(nom)+"?")
            n=menu(
                "1.Si\t2. No",
                "Escribe el número asociado tu respuesta", 
                1, 2)
    print("\n¡Perfecto!\n")
    if (p==1):
        pokedex.capturar(1)
        especie="BULBASAUR"
    elif (p==2):
        pokedex.capturar(4)
        especie="CHARMANDER"
    elif (p==3):
        pokedex.capturar(7)
        especie="SQUIRTLE"

    if (n==1):
        nombre=nom
    elif (n==2):
        nombre=especie

    primigenio=Pokemon(nombre, especie, pokedex)

    pokemones.eliminarFila(0)

    primigenio.capturar(pokedex, pokemones, 5)

    pokedex.exportar()
    pokemones.exportar()


opcion=1
while(opcion!=5):
    opcion=menu(
            "\n1.Ver Pokedex\n2.Inventario Pokemon\n3.Combate con un rival\n4.Explora y ecuentra un pokemon nuevo\n5.Guardar y Salir",
            "\nEscribe el número asociado tu respuesta ", 
            1, 5)
    if(opcion==1):
        print("\nHas descubierto "+str(pokedex.df['captura'].value_counts()[1])+" pokemon")
        print("\nAun hay "+str(pokedex.df['captura'].value_counts()[0])+" pokemon por descubrir\n")
        print("\nPokemones descubiertos:\n")
        count=0
        while(pokedex.filas>=count):
            if(pokedex.df.iloc[count,[7]][0]==1):
                print (str(pokedex.df.iloc[count,[0]][0])+" "+str(pokedex.df.iloc[count,[1]][0]))
            count+=1
        while(True):
            try:
                info=1
                while(info!=0):
                    info=menu(
                        "\n¿Deseas ver la información de algun pokemon?\n(Si no quieres ver la información de ningún pokemon, escribe 0)",
                        "\nEscribe el número asociado tu respuesta: ", 
                        0, 10)
                    if (info!=0):
                        pokemon=Pokemon(pokedex.encontrarNum(info),pokedex.encontrarNombre(info),pokedex)
                        print("\nN°: "+str(pokemon.num))
                        print("Nombre: "+str(pokemon.nombre))
                        print("Tipo: "+str(pokemon.tipo))
                        print("Descripción: "+str(pokemon.descripcion))
                break
            except IndexError:
                print("Información insuficiente, aun no has descubierto ese pokemon")
    elif(opcion==2):
        print("algo")
    elif(opcion==3):
        print("algo")
    elif(opcion==4):
        print("algo")
    elif(opcion==5):
        pokedex.exportar()
        pokemones.exportar()
        print("¡¡¡Adios!!!")
#("Tu pokemon es "+str(pokemones.df["nombre"][0][0])+" de especie "+str(pokemones.df["especie"][0][0]))
estadisticas("Aver")
explorar("Aver")
desafiar("Aver")



