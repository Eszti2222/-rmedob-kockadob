import random


"""
Készíts függvényt, mely az érmedobást szimulálja és generálj 10  db fej vagy írást  és  az eredméynt eltárolja egy
lsitában. A fv térjen vissza a listával.

A továbbiakban ezzel a listával dolgozz az alábbi függvényekben:
számold meg hány fej dobás van a listában

"""
"""
Készíts függvényt, mely az kockadobást szimulálja és generálj 200 db véletlen kockadobást  és  az eredméynt eltárolja egy
lsitában. A fv térjen vissza a listával.

A továbbiakban ezzel a listával dolgozz az alábbi függvényekben:
számold meg hányszor dobtunk egyest,kettest,....hatost!

Készíts 'cinkelt' kockát! A hatost nagyobb valószínűséggel dobja!
A cinkelt kockával is futtasd le a fenti fv-t. Kiderül a csalás?

"""
def erme_dobas():
    
    vlista=[]
    i:int=0
    
    while(i<10):
        vszam:int= int(random.random()*2+1)
        if(vszam==1):
            vlista.append("fej")
        else:
            vlista.append("írás")
        i+=1
    return vlista

def iras(vlista):
    iras:int=0
    i:int=0
    while(i<len(vlista)):
        if(vlista[i]=="írás"):
            iras+=1
        i+=1
    return iras

def fej(vlista):
    fej:int=0
    i:int=0
    while(i<len(vlista)):
        if(vlista[i]=="fej"):
            fej+=1
        i+=1
    return fej

#################################################
def kockadobas():
    kocka_lista=[]

    i:int= 0
    while(i<10):
        vdobások:int= int(random.random()*6+1)
        kocka_lista.append(vdobások)
        i+=1
    return kocka_lista

def mibol_mennyi_dobas(kocka_lista,szam):
    i:int=0
    db=0
    """egyes:int=0
    kettes:int=0
    harmas:int=0
    negyes:int=0
    otos:int= 0
    hatos:int=0
    while(i<len(kocka_lista)):
        if(kocka_lista[i]==1):
            egyes+=1
        elif(kocka_lista[i]==2):
            kettes+=1
        elif(kocka_lista[i]==3):
            harmas+=1
        elif(kocka_lista[i]==4):
            negyes+=1
        elif(kocka_lista[i]==5):
            otos+=1
        else:
            hatos+=1
        i+=1
    dblista.append(egyes)
    dblista.append(kettes)
    dblista.append(harmas)
    dblista.append(negyes)
    dblista.append(otos)
    dblista.append(hatos)
    return dblista"""
    while(i<len(kocka_lista)):
        if(kocka_lista[i]==szam):
            db+=1
        i+=1
    return db
    


'''def kiir(dblista):
    kiirlista=[]
    i:int=0
    while(i<len(dblista)):
        if()'''
        









