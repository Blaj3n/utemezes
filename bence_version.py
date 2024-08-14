taborok = []

with open("taborok.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        # 6	26	7	10	GIOSY	foci
        egysor = egysor.strip().split()
        taborok.append([int(egysor[0]), int(egysor[1]), int(egysor[2]), int(egysor[3]), str(egysor[4]), str(egysor[5])])
# print(taborok)

print("2. feladat ")
print(f"Az adatsorok száma: {len(taborok)} ")
print(f"Az először rögzített tábor témája: {taborok[0][5]} ")
print(f"Az utoljára rögzített tábor témája: {taborok[len(taborok)-1][5]} ")

print("3. feladat ")
zenei_tabor = []
for egyelem in taborok:
    if egyelem[-1] == "zenei":
        print(f"Zenei tábor kezdődik {egyelem[0]}. hó {egyelem[1]}. napján. ")
        zenei_tabor.append(egyelem)

if len(zenei_tabor) == 0:
    print("Nem volt zenei tábor. ")