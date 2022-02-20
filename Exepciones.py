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