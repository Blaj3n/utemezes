taborok = []

with open("taborok.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        # 6	26	7	10	GIOSY	foci
        egysor = egysor.strip().split()
        taborok.append([int(egysor[0]), int(egysor[1]), int(egysor[2]), int(egysor[3]), str(egysor[4]), str(egysor[5])])
print(taborok)