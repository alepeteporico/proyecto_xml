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
    if elec==1:
        ejer1(doc)
        print("=============================")
        intro=input("Pulsa enter para continuar")
        print("")
    
    elif elec==2:
        equipo=input("¿Qué equipo eliges? ")
        heroes=doc.xpath("/Marvel/element/Teams/team/name/text(%c)/integrers",(equipo))
    elif elec==6:
        break