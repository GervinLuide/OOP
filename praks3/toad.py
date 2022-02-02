from praks3.tuba import *

print("Ruumi mõõtmed")
p = float(input("Pikkus: "))
l = float(input("Laius: "))
k = float(input("Kõrgus: "))



tuba = Tuba(p, l, k)

vastus = input("Kas olemas aknad/uksed jah/ei: ")
while vastus == "jah":
    l = float(input("Akna/Ukse laius "))
    k = float(input("Akna/Ukse kõrgus "))
    aken_uks = Aknad_ja_Uksed(l, k)
    tuba.aknad_uksed.append(aken_uks)
    vastus = input("Kas olemas aknad/uked? jah/ei ")

print("Tapeedi rulli mõõtmed: ")
tl = float(input("Tapeedi rulli laius "))
tp = float(input("Tapeedi rulli pikkus "))

print("Tapeedid on vaja kleepida " + str(tuba.tööpind()) + " ruutmeetrites")
print("Tapeedi rullide arv " + str(tuba.tapeedirull(tl, tp, tuba.tööpind())))

