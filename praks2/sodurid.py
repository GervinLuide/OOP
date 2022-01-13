from random import randint
from praks2.sodur import Sodur

sodur1 = Sodur()
sodur2 = Sodur()

while(sodur1.tervis > 0 and sodur2.tervis > 0):
    kes_loob = randint(1,2)
    if(kes_loob == 1):
        print("esimene lööb teist")
        sodur2.tervis -= 20
    if (kes_loob == 2):
        print("teine lööb esimest")
        sodur1.tervis -= 20

if(sodur1.tervis != 0):
    print("esimene on võitunud")
    print("Teine on kaotanud")
else:
    print("Teine on võitnud")
    print("Esimene on kaotanud")