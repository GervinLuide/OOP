class Kasutaja():
    def __init__(self, eesnim, pernim, van, meil):
        self.eesnimi = eesnim
        self.perenimi = pernim
        self.vanus = van
        self.mail = meil


    sisselogimiskatsed = 0

    def suurenda_sisselogimiskatsed(self, sisselogimiskatsed):
        self.sisselogimiskatsed += sisselogimiskatsed

    def reset_sisselogimiskatsed(self):
        self.sisselogimiskatsed = 0

    def kirjelda_kasutaja(self):
        print("Ees ja perekonnanimi " + self.eesnimi + " " + self.perenimi)
        print("Vanus " + self.vanus)
        print("Email " + self.mail)

    def tervita_kasutaja(self):
        print("Tere tulemast " + self.eesnimi + "!")