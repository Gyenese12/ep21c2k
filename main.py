file = open("valaszok.txt", "r")
Lista = []
Listakod = []
Listavalasz = []
temp = 0
for i in file.readlines():
    Lista.append(i)
    Listakod.append(i[0, 4])
    Listavalasz.append(i[6, 19])
    temp += 1
print("1. feladat: Adatok beolvasva")
print(f"2. feladat: A versenyen {temp-1} versebyző indult")
Listakod.remove([0])
Listavalasz.remove([0])

#feladat3
kod = input("3. feladat: Kérem adja meg a versenyző azonosítóját: ")
st = 0
kodja = ""
segit = 0
for i in Listakod:
    segit+=1
    if(i == kod):
        print(Listavalasz[segit])
        kodja = Listavalasz
        st+=1

if(st == 0):
    print("Ilyen kóddal nem indult versenyző")
    kodja = Listavalasz[0]

#feladat4
print(f"4. feladat: A helyes megoldás: {Lista[0]}")
temp2 = 0
f4 = ""
for s in range(len(kodja)):
    if Lista[0][temp2] == kodja[s]:
        temp2 +=1
        f4 += "+"
    else:
        f4 += " "
print(f4)


#feladat5
sorszam = int(input("Kérem egy feladat sorszámát"))
Megoldas = Lista[0]
helyes = 0

for i in Listavalasz:
    if(i[sorszam] == Megoldas[sorszam]):
        helyes +=1
print("A versenyzők {}%-a válaszolt helyesn".format(((helyes)/temp-1*100)))



#feladat6
temp = 0
file2 = open("pontok.txt", "a")
for i in Listavalasz:
     seged = i
     temp3 = ""
     megold = 0
     for r in range(14):
         if (seged[r] == Megoldas[r] and r < 6):
             megold += 3
         if (seged[r] == Megoldas[r] and r > 5 and r < 11) :
             megold+= 4
         if(seged[r] == Megoldas[r] and r > 10 and r < 14) :
             megold += 5
         if(seged[r] == Megoldas[r] and r == 14) :
             megold += 6
     temp3 = f"{Listakod[temp]} {megold}"
     temp+=1
     file2.write(temp3)


#feladat7
print("7. feladat: A verseny legjobbjai")
file2.flush()
temp = 0
seged = ""
max = 0
Listaeredmeny = []
for i in file2.readlines() :
    Listaeredmeny.append(i)
    if (int(i[7,8]) > max) :
        max = int(i[7,8])

temp = 0
for i in Listaeredmeny :
    temp+=1
    if (i[7,8] == max) :
        print(f"1. díj ({max} {Listakod[temp]})")
        Listaeredmeny.remove(i)
max = 0
for i in Listaeredmeny :
    if(i[7,8] > max) :
        max = i[7,8]
temp = 0
for i in Listaeredmeny :
    if (i[7,8] == max) :
        print(f"2. díj ({max} {Listakod[temp]})")
        temp+=1
        Listaeredmeny.remove(i)

max = 0
temp = 0
for i in Listaeredmeny:
    if (i[7, 8] > max):
        max = i[7, 8]
temp = 0
for i in Listaeredmeny:
    temp+=1
    if (i[7, 8] == max):
        print(f"3. díj ({max} {Listakod[temp]})")
file.close()
file2.close()














