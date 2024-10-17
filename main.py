import feladatok
import veletlenszamos_listak
lista=[12,21,56,32, -5, -23,35]


print("1.feladat")
db: int=feladatok.poz_szamok_szama(lista)
print(f"A pozitív számok száma {db}")

print("2.feladat")
ossz: int= feladatok.negativ_szamok_osszege(lista)
print(f"A negatív számok összege {ossz}")

print("3.feladat")
atlag:float= feladatok.ottel_oszthato_osszege(lista)
print(f"Az öttel osztható számok átlaga {atlag}")

print("4.feladat érmedobás")
vlista:int= veletlenszamos_listak.erme_dobas()
fejek:int = veletlenszamos_listak.fej(vlista)
irasok:int = veletlenszamos_listak.iras(vlista)
print(f"Az érmedobások: {vlista}")
print(f"Fej {fejek} db ; Írás {irasok} db")

print("5.feladat kockadobás")
kocka_lista:int= veletlenszamos_listak.kockadobas()
#dblista:int= veletlenszamos_listak.mibol_mennyi_dobas(kocka_lista)
print(f"A dobások:{kocka_lista}")
#veletlenszamos_listak.kiir()
#print(f"nhjhjk {dblista}")
db:int= veletlenszamos_listak.mibol_mennyi_dobas()
veletlenszamos_listak.mibol_mennyi_dobas(db,1)
veletlenszamos_listak.mibol_mennyi_dobas(db,2)
veletlenszamos_listak.mibol_mennyi_dobas(db,3)
veletlenszamos_listak.mibol_mennyi_dobas(db,4)
veletlenszamos_listak.mibol_mennyi_dobas(db,5)
veletlenszamos_listak.mibol_mennyi_dobas(db,6)

