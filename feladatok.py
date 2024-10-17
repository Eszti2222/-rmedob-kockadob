"""adott egy lista 
lista=[12,21,56,32, -5, -23,35]
Az alábbi metódusok paraméterként kapják a fenti listát.
1.Hány ppozitív szám van benne?
2.Mennyi a negatív számok összege?
3.Mennyi az öttel osztható számok átlaga?"""

def poz_szamok_szama(lista):
    
    i:int =0
    db:int =0
    while(i<len(lista)):
        if(lista[i]>0):
            "print(lista[i], end=";")"
            db+=1
        i+=1
    return db

def negativ_szamok_osszege(lista):
    i:int=0
    ossz:int=0
    while(i<len(lista)):
        if(lista[i]<0):
            ossz+=lista[i]
        i+=1   
    return ossz

def ottel_oszthato_osszege(lista):
    i:int=0
    osszeg:int=0
    db:int=0
    
    while(i<len(lista)):
        if(lista[i]%5==0):
            osszeg+=lista[i]
            db+=1
        i+=1
    atlag:float=osszeg/db
    return atlag