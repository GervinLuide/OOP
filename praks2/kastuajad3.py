from praks2.kasutaja3 import Kasutaja

kasutaja = Kasutaja("Gervin", "Luide", "17", "gervin.luide@voco.ee")

kasutaja.kirjelda_kasutaja()
kasutaja.tervita_kasutaja()

print(kasutaja.suurenda_sisselogimiskatsed(3))
kasutaja.suurenda_sisselogimiskatsed(6)
print("Olete sisseloginud", kasutaja.sisselogimiskatsed, "korda ")

kasutaja.reset_sisselogimiskatsed()
print(kasutaja.sisselogimiskatsed)