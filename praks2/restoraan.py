class Restoraan():
    restoraani_nimi = ""
    soogi_tyyp = ""

    def kirjelda_restoraan(self):
        print("Restoraan " + self.restoraani_nimi + " pakub " + self.soogi_tyyp)

    def ava_restoraan(self):
        print("restoraan on avatud")