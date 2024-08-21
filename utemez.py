# print("1. feladat ")
taborok = [] # Elsőként létre kell hozni egy üres listát, egy ütős névvel.
# a with-del előhívom a beépített "open" metódust, amibe 3 adatot beírok:
# open("a_txt_neve.txt", "r" <- két fajta lehet, a beolvasáshoz "r": read, az íráshoz, lásd a további feladatok közt "w": write, és a végén encoding="utf-8" <- ez fontos)
# "as" annyit tesz, hogy az előbb leírtakat többször nem kell leírni, csupán, ha megadok neki egy nevet (file) akkor simán csak a file néven hivatkozhatok rá.
with open("taborok.txt", "r", encoding="utf-8") as file:
    # 6   26    7	10	GIOSY	foci
    for egysor in file:
        egysor = egysor.strip().split()
        taborok.append([int(egysor[0]), int(egysor[1]), int(egysor[2]), int(egysor[3]), str(egysor[4]), str(egysor[5])])
print(taborok)

# indítok egy ciklust (for egysor in file:) (egysor: 6   26    7	10	GIOSY	foci)
# egysor = egysor.strip() <- megszabadítja a felesleges "   " szóközöktől, tehát innentől kezdve a közöttes tabulátorok, ezek nem lesznek karakterként bejegyezve. A split() metódus pedig listává teszi, és innentől értelmezhetővé válik a pl.: egysor[0], egysor[5]
# a taborokba beletesszük (append metódussal) egyenként. Ami int, azt érdemesebb már itt megnevezni, ami string, azt str.
# taborok = [[egysor]], 6, 'GIOSY' ez lesz egyeleme az egysornak.

print("2. feladat ")
print(f"Az adatsorok száma: {len(taborok)} ")
print(f"Az először rögzített tábor témája: {taborok[0][-1]} ")
print(f"Az utoljára rögzített tábor témája: {taborok[-1][-1]} ")
# a -1 az utolsó.

# 6   26    7	10	GIOSY	foci
print("3. feladat ")
zenei_tabor = False
for egyelem in taborok:
    if egyelem[-1] == "zenei":
        print(f"Zenei tábor kezdődik {egyelem[0]}. hó {egyelem[1]}. napján. ")
        zenei_tabor = True

if not zenei_tabor:
    print("Nem volt zenei tábor. ")


print("4. feladat ")
print("Legnépszerűbbek: ")

legtobb_tabor = []
for tabor in taborok:
    legtobb_tabor.append([tabor[0], tabor[1], len(tabor[4]), tabor[5]])
print(legtobb_tabor)

jelentkezok = []
for tabor in taborok:
    jelentkezok.append(len(tabor[4]))
print(f"Jelentkezők: {jelentkezok} ")
max_jelentkezok = max(jelentkezok)
print(max_jelentkezok)

for egyelem in legtobb_tabor:
    if egyelem[2] == max_jelentkezok:
        print(f"{egyelem[0]} {egyelem[1]} {egyelem[-1]}")

# print("5. feladat ")

def sorszam(honap:int, nap:int):
    if honap == 6:
        return nap - 16
    elif honap == 7:
        return (30-16) + nap
    elif honap == 8:
        return (30-16+32) + nap  # tehát a 0. naptól kezdődik így egyel meg lesz növelve az egész.
print(sorszam(8,1))

print("6. feladat ")
ho = int(input("hó: "))
napja = int(input("nap: "))
szam = sorszam(ho, napja)
print(szam)

# 6	26	7	10	GIOSY	foci

lista = []
for tabor in taborok:
    lista.append([sorszam(tabor[0], tabor[1]), sorszam(tabor[2], tabor[3])])
print(lista)

szamlalo = 0
for elem in lista:
    if elem[0] <= szam <= elem[1]:
        szamlalo += 1
print(f"Ekkor éppen {szamlalo} tábor tart.")