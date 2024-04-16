Zbozi = ["mliko", "jablko", "voda", "kolac", "rizek"]
Zbozi1 = ["mliko", "jablko", "voda", "kolac", "rizek"]
print ("----------------------------------------")
print ("vítejte u terminálu, napište číslo pro zvolení zboží (0 až 4)")
print ("----------------------------------------")
for x in Zbozi:
    print(x)
print ("----------------------------------------")

vyber = input("pro výběr do košíku napište číslo: ")
vyber = int(vyber)

def odebrat(odebrat):
    Zbozi.pop(odebrat)
    print (Zbozi)
    return

def košíku(m):
    print (Zbozi1[m])
    return



print ("----------------------------------------")
odebrat(vyber)
print ("----------------------------------------")

print ("Zde je váš nákup")
košíku(vyber)

rozhodnutí = input("chcete pokračovat v nákupu? (ano/ne): ")
if rozhodnutí == "ano":
    vyber2 = input("který z zbývajicích zboží chcete?")
    vyber2 = int(vyber2)
    print ("----------------------------------------")
    odebrat(vyber2)
    print ("----------------------------------------")
    print ("Zde je váš nákup")
    košíku(vyber2)