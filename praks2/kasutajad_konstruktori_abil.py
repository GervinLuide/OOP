class Kasutaja():


    def __init__(self, eesnimi, perenimi, vanus):
        self.kasutaja_nimi = eesnimi
        self.kasutaja_perenimi = perenimi
        self.kasutaja_vanus = vanus

    def kirjelda_kasutaja(self):
        print("ees-ja perekonnanimi " + self.kasutaja_nimi + " " + self.kasutaja_perenimi)
        print("sinu vanus " + self.kasutaja_vanus)
        print("")

    def tervita_kasutaja(self):
        print("Tere tulemast " + self.kasutaja_nimi + "!")
        print("")