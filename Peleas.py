from random import randint
from Exepciones import menu
from Inicio import ponerNombre
import pandas as pd
def pelea(elegido, salvaje, ataques):
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
    "Escribe el número asociado al ataque que quieres realizar: ", 
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

def contra(elegido, salvaje, ataques):
    maxhabilidades=0
    if (salvaje.ataqueA != "Ninguno"):
        maxhabilidades+=1
        print(elegido.ataqueA)
    if (salvaje.ataqueB != "Ninguno"):
        maxhabilidades+=1
        print(elegido.ataqueC)
    if (salvaje.ataqueC != "Ninguno"):
        maxhabilidades+=1
        print(elegido.ataquC)
    if (salvaje.ataqueD != "Ninguno"):  
        maxhabilidades+=1
        print(elegido.ataqueD)
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

def pokebola(elegido, salvaje, ataques, pokedex, pokemones):
    print("Has lanzado una pokebola")
    print("...")
    porcentajeminimo=pokedex.df.set_index("nombre").loc[salvaje.nombre, "vida_total"]/10
    if (salvaje.vidaActual <= porcentajeminimo):
        print("¡Lo has capturado!")
        nombre=ponerNombre(salvaje.especie, pokemones)
        salvaje.nombre=nombre
        salvaje.vidaActual = pokedex.df.set_index("nombre").loc[salvaje.especie, "vida_total"]
        salvaje.lvl=salvaje.lvl+3
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

def desafio(elegido, rival, ataques):
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
    "Escribe el número asociado al ataque que quieres realizar: ", 
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


def explorar(pokedex):
    contador=pokedex.filas
    arrayGrandote={}
    grand= pd.DataFrame(arrayGrandote)
    while(contador>=0):
        aparicion=pokedex.df["aparicion"].array[contador]
        if (aparicion!=7):
            while(aparicion>0):
                arrayChiquito={'num':[pokedex.df["num"].array[contador]]}
                petit= pd.DataFrame(arrayChiquito)
                aparicion-=1
                grand=pd.concat([grand,petit],ignore_index=True)
        contador-=1
    aleatorio=randint(0,grand["num"].array.shape[0]-1)
    salvaje= grand.iloc[aleatorio, 0]
    return salvaje