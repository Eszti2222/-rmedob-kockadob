"""adott egy lista 
lista=[12,21,56,32, -5, -23,35]
Az alábbi metódusok paraméterként kapják a fenti listát.
1.Hány ppozitív szám van benne?
2.Mennyi a negatív számok összege?
3.Mennyi az öttel osztható számok összege?"""

def poz_szamok_szama(lista):
    
    i:int =0
    db:int =0
    while(i<len(lista)):
        if(lista[i]>0):
            "print(lista[i], end=";")"
            db+=1
        i+=1
    return db