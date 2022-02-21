#Importación de paquetes
from Json import DataFrame
from Pokemones import Pokemon
from Exepciones import menu
from random import randint
#importación de Data Frames
pokedex=DataFrame("Pokedex")
pokemones=DataFrame("Pokemon")
ataques=DataFrame("Ataques")
npc=DataFrame("NPC")

"""df2.set_index('Nombre', inplace=True)"""
#Si no tienes ningún pokemón, o sea, si la partida es nueva, Oak te da tu nuevo pokemon
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
                "Escribe el número asociado tu respuesta:", 
                1, 2)
    print("\n¡Perfecto!")
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
    primigenio=Pokemon(nombre, especie, 5, pokedex, pokemones, ataques)
    pokemones.eliminarFila(0)
    primigenio.capturar(pokedex, pokemones)
    pokedex.exportar()
    pokemones.exportar()


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
                        pokemon=Pokemon(pokedex.encontrarEspecie(info),pokedex.encontrarEspecie(info),5,pokedex,pokemones, ataques)
                        print("\nN°: "+str(pokemon.num))
                        print("Nombre: "+str(pokemon.nombre))
                        print("Tipo: "+str(pokemon.tipo))
                        print("Descripción: "+str(pokemon.descripcion))
                break
            except IndexError:
                print("Información insuficiente, aun no has descubierto ese pokemon")



    #Ver tus pokemones
    elif(opcion==2):
        print("algo")



    #Pelear con un rival    
    elif(opcion==3):
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
            print("\n¿Cuál ataque usarás a continuación?\n")
            maxhabilidades=4
            if (elegido.ataqueA != "Ninguno"):
                print("1. "+str(elegido.ataqueA))
            else:
                maxhabilidades-=1
            if (elegido.ataqueB != "Ninguno"):
                print("2. "+str(elegido.ataqueB))
            else:
                maxhabilidades-=1
            if (elegido.ataqueC != "Ninguno"):
                print("3. "+str(elegido.ataqueC))
            else:
                maxhabilidades-=1
            if (elegido.ataqueD != "Ninguno"):
                print("4. "+str(elegido.ataqueD))
            else:
                maxhabilidades-=1
            habilidad=menu(
            "",
            "Escribe el número asociado al ataque que queires realizar: ", 
            1, maxhabilidades)
            rival.recibirDaño(elegido.atacar(habilidad, ataques))
            if(habilidad==1):
                habilidad=elegido.ataqueA
            elif(habilidad==2):
                habilidad=elegido.ataqueB
            elif(habilidad==3):
                habilidad=elegido.ataqueC
            elif(habilidad==4):
                habilidad=elegido.ataqueD
            print(str(elegido.nombre)+" ha usado "+str(habilidad))
            print("La vida del rival ha bajado a "+str(rival.vidaActual))
            if(rival.vidaActual>=0):
                maxhabilidades=0
                if (elegido.ataqueA != "Ninguno"):
                    maxhabilidades+=1
                if (elegido.ataqueB != "Ninguno"):
                    maxhabilidades+=1
                if (elegido.ataqueC != "Ninguno"):
                    maxhabilidades+=1
                if (elegido.ataqueD != "Ninguno"):  
                    maxhabilidades+=1
                defensa=randint(1, maxhabilidades)
                elegido.recibirDaño(rival.atacar(defensa, ataques))
                if(defensa==1):
                    defensa=rival.ataqueA
                elif(defensa==2):
                    defensa=rival.ataqueB
                elif(defensa==3):
                    defensa=rival.ataqueC
                elif(defensa==4):
                    defensa=rival.ataqueD
                filtro = ataques.df["nombre"] == defensa
                defensa = ataques.df[filtro].iloc[0,0]
                print(str(rival.nombre)+" ha usado "+str(defensa))
                print("Tu vida ha bajado a "+str(elegido.vidaActual))
                if(elegido.vidaActual<=0):
                    print("oh no, u are dead")
            else:
                print("¡El rival se ha quedado sin fuerzas!\n¡Has ganado!")
        elegido.vidaActual = pokedex.df.iloc[elegido.num,3]

    #Buscar otros pokemons en la naturaleza  
    elif(opcion==4):
        aparicion=randint(0,9)
        print("Ha aparecido un\n" + str(pokedex.df.iloc[aparicion,1]) + " salvaje")
        print("¿Qué pokemon seberías usar? \n")
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
        salvaje=Pokemon(pokedex.df.iloc[aparicion,1],pokedex.df.iloc[aparicion,1],elegido.lvl-3,pokedex, pokemones,ataques)
        while(salvaje.vidaActual > 0 and elegido.vidaActual > 0):

            accion=menu(
            "¿Quieres pelear o intentar capturarlo?\n1. Pelear\t2. Capturar",
            "Escribe el número asociado a la acción que deseas realizar ", 
            1, 2)
            if(accion==1):
                print("\n¿Cuál ataque usarás a continuación?\n")
                maxhabilidades=4
                if (elegido.ataqueA != "Ninguno"):
                    print("1. "+str(elegido.ataqueA))
                else:
                    maxhabilidades-=1
                if (elegido.ataqueB != "Ninguno"):
                    print("2. "+str(elegido.ataqueB))
                else:
                    maxhabilidades-=1
                if (elegido.ataqueC != "Ninguno"):
                    print("3. "+str(elegido.ataqueC))
                else:
                    maxhabilidades-=1
                if (elegido.ataqueD != "Ninguno"):
                    print("4. "+str(elegido.ataqueD))
                else:
                    maxhabilidades-=1
                habilidad=menu(
                "",
                "Escribe el número asociado al ataque que queires realizar: ", 
                1, maxhabilidades)
                salvaje.recibirDaño(elegido.atacar(habilidad, ataques))
                if(habilidad==1):
                    habilidad=elegido.ataqueA
                elif(habilidad==2):
                    habilidad=elegido.ataqueB
                elif(habilidad==3):
                    habilidad=elegido.ataqueC
                elif(habilidad==4):
                    habilidad=elegido.ataqueD
                print(str(elegido.nombre)+" ha usado "+str(habilidad))
                print("La vida del pokemon salvaje ha bajado a "+str(salvaje.vidaActual))
                if(salvaje.vidaActual>=0):
                    maxhabilidades=0
                    if (elegido.ataqueA != "Ninguno"):
                        maxhabilidades+=1
                    if (elegido.ataqueB != "Ninguno"):
                        maxhabilidades+=1
                    if (elegido.ataqueC != "Ninguno"):
                        maxhabilidades+=1
                    if (elegido.ataqueD != "Ninguno"):  
                        maxhabilidades+=1
                    defensa=randint(1, maxhabilidades)
                    elegido.recibirDaño(salvaje.atacar(defensa, ataques))
                    if(defensa==1):
                        defensa=salvaje.ataqueA
                    elif(defensa==2):
                        defensa=salvaje.ataqueB
                    elif(defensa==3):
                        defensa=salvaje.ataqueC
                    elif(defensa==4):
                        defensa=salvaje.ataqueD
                    filtro = ataques.df["nombre"] == defensa
                    defensa = ataques.df[filtro].iloc[0,0]
                    print(str(salvaje.nombre)+" ha usado "+str(defensa))
                    print("Tu vida ha bajado a "+str(elegido.vidaActual))
                    if(elegido.vidaActual<=0):
                        print("oh no, u are dead")
                else:
                    print("¡El salvaje se ha quedado sin fuerzas!\n¡Has ganado!")
            else:
                print("Has lanzado una pokebola")
                print("...")
                porcentajeminimo=pokedex.df.iloc[salvaje.num,3]/10
                if (salvaje.vidaActual <= porcentajeminimo):
                    print("¡Lo has capturado!")
                    salvaje.capturar(pokedex, pokemones)
                    pokedex.capturar(salvaje.num)
                    salvaje.vidaActual = 0
                else:
                    print("¡Oh no! "+str(salvaje.nombre)+" se ha liberado")
                    maxhabilidades=0
                    if (elegido.ataqueA != "Ninguno"):
                        maxhabilidades+=1
                    if (elegido.ataqueB != "Ninguno"):
                        maxhabilidades+=1
                    if (elegido.ataqueC != "Ninguno"):
                        maxhabilidades+=1
                    if (elegido.ataqueD != "Ninguno"):  
                        maxhabilidades+=1
                    defensa=randint(1, maxhabilidades)
                    elegido.recibirDaño(salvaje.atacar(defensa, ataques))
                    if(defensa==1):
                        defensa=salvaje.ataqueA
                    elif(defensa==2):
                        defensa=salvaje.ataqueB
                    elif(defensa==3):
                        defensa=salvaje.ataqueC
                    elif(defensa==4):
                        defensa=salvaje.ataqueD
                    filtro = ataques.df["nombre"] == defensa
                    defensa = ataques.df[filtro].iloc[0,0]
                    print(str(salvaje.nombre)+" ha usado "+str(defensa))
                    print("Tu vida ha bajado a "+str(elegido.vidaActual))
                    if(elegido.vidaActual<=0):
                        print("oh no, u are dead")
        salvaje.vidaActual = pokedex.df.iloc[salvaje.num,3]
        elegido.vidaActual = pokedex.df.iloc[elegido.num,3]
    #Salir y guardar tus datos
    elif(opcion==5):
        pokedex.exportar()
        pokemones.exportar()
        print("¡¡¡Adios!!!")



