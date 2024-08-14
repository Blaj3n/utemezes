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
