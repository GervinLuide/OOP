#mooduli importimine
from random import randint
#klasside loomine
class Andmed:
    """Andmete hoidmise klass"""
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]

class Opetaja:
    """Õpetaja klass õpetab õpilastele andmeid"""
    def opetab(self, info, *opilane):
        """Õpetab teadmisi õpilastele, vajab õpetava infot ja õpilaste nimesid"""
        for i in opilane:
            i.opib(info)

class Opilane:
    """klass, mis hoiab õpitud teadmisi"""
    def __init__(self):

        self.teadmised = []
    def opib(self, info):
        """Õpetab teadmisi õpilastele, vajab õpetava infot, prindib õpitud teema"""
        self.teadmised.append(info)
        print("Õpilane õppis teema " + info)
    def unustab(self):
        """Kusututab teadmised õpilase objektist"""
        voimalus = randint(1, 10)
        if voimalus <= 5:
            """kustutab teadmised ja prindib unsutatud teema"""
            voimalus2 = randint(0, len(self.teadmised) - 1)
            print("Õpilane unustas teema " + self.teadmised[voimalus2])
            self.teadmised.pop(voimalus2)

        else:
            pass

