class Kasutaja():
    eesnimi = ""
    perenimi = ""
    email = ""
    sunnikuupaev = ""

    def kirjelda_kasutaja(self):
        print("ees-ja perekonnanimi " + self.eesnimi + " " +self.perenimi)
        print("sinu email " + self.email)
        print("sünnikuupäev " + self.sunnikuupaev)
        print("")

    def tervita_kasutaja(self):
        print("Tere tulemast " + self.eesnimi + "!")
