from praks2.restoranid3 import Restoraan
class JaatiseKiosk(Restoraan):
    jaatise_valik = ""
    def naita_jaatise_valik(self):
        print(self.jaatise_valik)