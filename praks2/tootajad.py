class Inimene():

    def __init__(self, eesnimi, perenimi, kutsekvalifikatsioon = 1):
        self.inimene_eesnimi = eesnimi
        self.inimene_perenimi = perenimi
        self.inimene_kvl = kutsekvalifikatsioon

    def __del__(self):
        print("Kõike head")

    def tutvustus(self):
        print("Tere, olen", self.inimene_eesnimi, self.inimene_perenimi)

