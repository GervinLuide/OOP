class Restoraan():

    def __init__(self, restoraani_nimi, soogi_tyyp):
        self.restorani_nimi = restoraani_nimi
        self.soogi_tuup = soogi_tyyp

    def kirjelda_restoraan(self):
        print("Restoraan " + self.restorani_nimi + " pakub " + self.soogi_tuup)

    def ava_restoraan(self):
        print("restoraan on avatud")
