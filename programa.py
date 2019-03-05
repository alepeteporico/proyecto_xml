from lxml import etree
doc=etree.parse('marvel.xml')

def ejer1(doc):
    pers=input("¿Qué quieres listar: heroes, villanos o equipos? ")
    if pers=="heroes":
        lista=doc.xpath("/Marvel/element/heroes/character/hero/text()")
    elif pers=="villanos":
        lista=doc.xpath("/Marvel/element/Villains/character/hero/text()")
    elif pers=="equipos":
        lista=doc.xpath("/Marvel/element/Teams/team/name/text()")
    for nombre in lista:
        print("-",nombre)
    print("")

def ejer2 (doc):
    equipo=input("¿Qué equipo eliges? ")
    heroes=doc.xpath("/Marvel/element/Teams/team[name='{}']/integrers/@miembros".format(equipo))
    lista=heroes[0].split(",")
    print(len(lista),"héroes conforman este equipo")
    print("")

def ejer3 (doc):
    equipo=input("¿Qué equipo eliges? ")
    heroes=doc.xpath("/Marvel/element/Teams/team[name='{}']/integrers/@miembros".format(equipo))
    lista=heroes[0].split(",")
    print("el equipo {} lo conforman:".format(equipo))
    for heroe in lista:
        print("-",heroe)
    print("")

def ejer4 (doc):
    villano=input("¿Que villano eliges? ")
    enemigo=doc.xpath("/Marvel/element/Villains/character[hero='{}']/enemigo/text()".format(villano))

    lista1=doc.xpath("/Marvel/element/heroes/character/hero/text()")
    lista2=doc.xpath("/Marvel/element/Teams/team/name/text()")

    if enemigo[0] in lista1:
        nombre=doc.xpath("/Marvel/element/heroes/character[hero='{}']/name/text()".format(enemigo[0]))
        print("Su mayor enemigo es {} álias {}".format(enemigo[0],nombre[0]))
    elif enemigo[0] in lista2:
        heroes=doc.xpath("/Marvel/element/Teams/team[name='{}']/integrers/@miembros".format(enemigo[0]))
        lista=heroes[0].split(",")

        print("Su mayor enemigo son los {} quienes integran a:".format(enemigo[0]))

        for heroe in lista:
            print("-",heroe)
    print("")

while True:
    print("================================================================================")
    print("1.Listar los nombres de héroes, villanos o equipos a nuestra elección.")
    print("2.Contar cuantos héroes forman un equipo a nuestra elección.")
    print("3.pedir por teclado un equipo y te muestre los héroes que lo forman.")
    print("4.Pedir un villano por teclado y te muestra su mayor enemigo (En caso de ser un solo héroe te mostrará su nombre real, en caso de ser un equipo te mostrará quienes lo forman).")
    print("5.Pide por teclado un villano, héroe o equipo y ejecuta una ventana en el navegador que te muestra la biografía del mismo.")
    print("6.Salir")
    print("================================================================================")
    elec=int(input("Elige una opción: "))
    print("")
    if elec==6:
        break
  
    elif elec==1:
        ejer1(doc)
        print("------------------------------")
        intro=input("Pulsa enter para continuar")
        print("")
    
    elif elec==2:
        ejer2(doc)
        print("-----------------------------")
        intro=input("Pulsa enter para continuar")
        print("")
    
    elif elec==3:
        ejer3(doc)
        print("-----------------------------")
        intro=input("Pulsa enter para continuar")
        print("")
    
    elif elec==4:
        ejer4(doc)    
        print("-----------------------------")
        intro=input("Pulsa enter para continuar")
        print("")