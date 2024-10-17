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







