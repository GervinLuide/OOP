from praks3.aknadjauksed import Aknad_ja_Uksed

class Tuba():
    def __init__(self, pikkus, laius, korgus):

        self.pikkus = pikkus
        self.laius = laius
        self.korgus = korgus

        self.aknad_uksed = []

    def lisaAkkenUks(self, laius, korgus):
        self.aknad_uksed.append(Aknad_ja_Uksed(laius, korgus))

    def pindalad(self, pikkus, laius, korgus):
        pindala = 2 * korgus * (pikkus + laius)
        return pindala

    def tapeedirull(self, tapeedirulli_laius, tapeedirulli_pikkus, tööpind):
        rulli_pindala = tapeedirulli_laius * tapeedirulli_pikkus
        rullidearv = round(tööpind / rulli_pindala)
        return rullidearv


    def tööpind(self):
        uus_pindala = self.pindalad(self.pikkus, self.laius, self.korgus)
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
        return uus_pindala

