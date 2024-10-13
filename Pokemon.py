#   ACTIVIDAD PRÁCTICA PYTHON TRIMESTRE 3 
#   Luis Guillermo Gonzales Carrillo
#   JUEGO DE POKEMON

from random import randint #importo la libreria de ramdom para poder utilizarla en mi metodo

#Lista de pokemon por defecto
pokemon = ['Pikachu','Bulbasaur','Charmander','Squirtle','Lucario','Greninja','Gengar','Onix','Exeggcute','Rhyhorn','Staryu','Eevee']
#lista de poderes de pokemones en general
poderes =['Gruñido', 'Rugido','Placaje','Destructor','Arañazo']
#variable que utilizaré en pelea que lo inicializo
apelear = ""

# Función que me agrega un pokemon a la lista de pokemon
def agregar_pokemon(nombre_pokemon):
    pokemon.append(nombre_pokemon)
    return 'Se ha agregado correctamente el pokemon'

# Función que me elimina un pokemon de la lista de pokemon
def eliminar_pokemon(a_eliminar):
    pokemon.remove(a_eliminar)
    return 'Se ha ELIMINADO correctamente el pokemon'

def pelear():
    salvaje = pokemon[randint(0, len(pokemon) - 1)] #Eligo aleatoriamente un pokemon y saco su nombre
    print('Ha aparecido un', salvaje, 'Salvaje!!!!!!!!!!!!!!!')
    print('Se realizará una batalla pokemon entre', apelear.capitalize(), 'y', salvaje)
    
    #=====================================================================================
    #===================AQUI PONGO LA VIDA ALEATORIA DE LOS POKEMONES=====================
    #=====================================================================================
    vida = randint(50, 100)
    vidasalvaje = randint(50, 100)
    print('La vida de', apelear.capitalize(), 'es de:', vida)
    print('La vida de', salvaje, 'es de:', vidasalvaje)

    #=====================================================================================
    #===================AQUI PONGO EÑ DAÑO ALEATORIA DE LOS POKEMONES=====================
    #=====================================================================================
    continuar_pelea = True
    while vida > 0 and vidasalvaje > 0 and continuar_pelea:
        daño = randint(1, 50) #Hago un aleatorio entre 1 y 50 para el daño de pokemon
        dañosalvaje = randint(1, 50) #Hago un aleatorio entre 1 y 50 para el daño del pokemon salvaje

        #=========================================================================================
        #=============================DAÑO AL POKEMON ELEGIDO====================================
        #=========================================================================================

        print(apelear.capitalize(), 'ha realizado el ataque', poderes[randint(0, len(poderes) - 1)])
        print(apelear.capitalize(), 'ha realizado un daño de', daño)

        #RESTO LA VIDA DEL POKEMON SALVAJE ELEJIDO ALEATORIAMENTE
        vidasalvaje -= daño

        #COMPRUEBO LA VIDA DEL POKEMON SALVAJE
        #SI LA VIDA ES NEGATIVA LA PONGO A 0
        if vidasalvaje <= 0:
            print('Has ganado la batalla contra', salvaje, 'salvaje!!!!!')
            continuar_pelea = False
            break

        #=========================================================================================
        #=============================DAÑO AL POKEMON SALVAJE====================================
        #=========================================================================================

        print(salvaje, 'ha realizado el ataque', poderes[randint(0, len(poderes) - 1)])
        print(salvaje, 'ha realizado un daño de', dañosalvaje)
        #RESTO LA VIDA DEL POKEMON ELEGIDO
        vida -= dañosalvaje
        #SI LA VIDA ES NEGATIVA LA PONGO A 0
        if vida <= 0:
            print('Tu pokemon ha sido derrotado por', salvaje, 'Salvaje!!!!!!!!')
            continuar_pelea = False
        else:
            print('La vida de', apelear.capitalize(), 'es de:', vida)
            print('La vida de', salvaje, 'es de:', vidasalvaje)
    print('Fin de la batalla')


#Comienza la ejecucion del programa con su menú
repetir = True
while (repetir):
    print('*==========================================================*')
    print('*-------------Bienvenido al juego de Pokemon---------------*')
    print('*==========================================================*')
    print('*----------------- 1.Mostrar pokemon ----------------------*')
    print('*----------------- 2.Agregar pokemon ----------------------*')
    print('*--------------------- 3.Pelear ---------------------------*')
    print('*----------------- 4.Eliminar pokemon----------------------*')
    print('*----------------- 5.Salir del juego ----------------------*')
    print('*===========================================================')
    salir = True
    while (salir):
        opcion = int(input("Ingrese una opcion: "))
        #Si en caso mi opcion no es correcta a los parámetro la vuelvo a pedir
        if (opcion <= 0 or opcion >= 6):
            print('Ingrese una opción valida (1-5)')
        else:
            salir = False
            
    if(opcion == 1):
        print(pokemon)
        
    elif(opcion == 2):
        nombre_pokemon = input('Ingrese el nombre de su pokemon: ')
        print(agregar_pokemon(nombre_pokemon)) #llamo a mi funcion de agregar un pokemon en mi lista
        
    elif(opcion == 3):
        print('Los pokemones disponibles son: ')
        print('==========================================================')
        print(pokemon)
        print('==========================================================')
        apelear = input('Ingrese el nombre de su pokemon con el que desea pelear: ')

        pelear()

    elif(opcion == 4):
        print(pokemon) #muestro la lista
        nombre = input('Ingrese el nombre de su pokemon a eliminar: ') #pido el nombre a eliminar
        print(eliminar_pokemon(nombre.lower().capitalize())) #llamo a mi funcion de eliminar
        #El metodo capitalize() lo que hace es transformame a mayúscula mi primera letra
    elif(opcion == 5):
        print('Gracias por visitar nuestro juego')
        repetir = False