from Exepciones import menu
from Pokemones import Pokemon
def ponerNombre(especie, pokemones):
    n=2
    while (n==2):
        print("\n¿Te gustaría darle un nombre especial?")
        n=menu(
            "1.Si\t2. No\n",
            "Escribe el número asociado tu respuesta: ", 
            1, 2
        )
        if (n==1):   
            nom=input("\n¿Como te gustaría llamarle? ")
            for existente in pokemones.df["nombre"].unique():
                if (nom == existente):
                    print("\n¡Pero si ya tienes un pokemon con ese nombre!\n¡Se más original!") 
                    n=2
            if(n==1):
                print("\n¿Estás seguro de que quieres llamarle "+str(nom)+"?")
                n=menu(
                    "1.Si\t2. No",
                    "\nEscribe el número asociado tu respuesta: ", 
                    1, 2)
        elif (n==2):
            nom=especie
            for existente in pokemones.df["nombre"].unique():
                if (nom == existente):
                    print("¡Pero si ya tienes un pokemon con ese nombre!\n¡Se más original!")
                else:
                    print("\n¿Estás seguro?")
                    n=menu(
                        "1.Si\t2. No\n",
                        "Escribe el número asociado tu respuesta: ", 
                        1, 2
                    )
    if (n==1):
        nombre=nom
    elif (n==2):
        nombre=especie
    print("\n¡Perfecto!")
    return nombre

def inicio (pokedex, pokemones, ataques):
    print("\n¡Hola!\n¡Este es el mundo de los pokemon!\n¡Me llamo Oak!\n¡Pero la gente me llama Profesor Pokemon!")
    print("¡Aquí hay tres pokemon!\n¡Cuando yo era joven era un buen entrenador pokemon!")
    print("Pero ahora solo me quedan tres...\n \n¡Te dare uno! ¿Cuál quieres?\n")
    p=menu(
        "1. BULBASAUR\t2. CHARMANDER\t3. SQUIRTLE",
        "Escribe el número asociado al pokemon que te gusta más: ",
        1, 3)
    nombre=ponerNombre(p, pokemones)
    if (p==1):
        pokedex.capturar(1)
        especie="BULBASAUR"
    elif (p==2):
        pokedex.capturar(4)
        especie="CHARMANDER"
    elif (p==3):
        pokedex.capturar(7)
        especie="SQUIRTLE"
    primigenio=Pokemon(nombre, especie, 5, pokedex, pokemones, ataques)
    pokemones.eliminarFila(0)
    primigenio.capturar(pokedex, pokemones)
    pokedex.exportar()
    pokemones.exportar()