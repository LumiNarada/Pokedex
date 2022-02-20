from Json import DataFrame
from Pokemones import Pokemon
from Estadisticas import estadisticas
from Pelea import explorar, desafiar
from Exepciones import menu

pokedex=DataFrame("Pokedex")
pokemones=DataFrame("Pokemon")

"""df2.set_index('Nombre', inplace=True)"""

if (pokemones.df.loc[0]==NULL):
    print("\n¡Hola!\n¡Este es el mundo de los pokemon!\n¡Me llamo Oak!\n¡Pero la gente me llama Profesor Pokemon!")
    print("¡Aquí hay tres pokemon!\n¡Cuando yo era joven era un buen entrenador pokemon!")
    print("Pero ahora solo me quedan tres...\n \n¡Te dare uno! ¿Cuál quieres?\n")
    p=menu(
        "1. BULBASAUR\t2. SQUIRTLE\t3. CHARMANDER",
        "Escribe el número asociado al pokemon que te gusta más ",
        1, 3)
    print("\n¿Te gustaría darle un nombre especial?")
    n=menu(
        "1.Si\t2. No\n",
        "Escribe el número asociado tu respuesta ", 
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

