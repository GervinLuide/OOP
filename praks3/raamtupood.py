from praks3.raamat import Raamat

class Raamatupood():

    def __init__(self, nimi, reiting):
        self.nimi = nimi
        self.reiting = reiting


    raamatulist = []
    def saan_lisada_raamat(self, raamat):
        for raamatud in self.raamatulist:
            if raamat.autor == raamatud.autor:
                return False
            else:
                if raamat.pealkiri == raamatud.pealkiri:
                    return False
                else:
                    if raamat.reiting >= self.reiting:
                        return True

                    else:
                        pass
        return True

    def lisa_raamat(self, raamat):
        if self.saan_lisada_raamat(raamat) == True:
            self.raamatulist.append(raamat)

        elif self.saan_lisada_raamat(raamat) == False:
            print("Seda raamatut ei saa lisada")


    def saan_eemaldada_raamat(self, raamat):
        for raamatud in self.raamatulist:
            if raamat.autor == raamatud.autor and raamat.pealkiri == raamatud.pealkiri:
                return True
            else:
                return False

    def eemalda_raamat(self, raamat):
        if self.saan_eemaldada_raamat(raamat) == True:
            self.raamatulist.remove(raamat)
            print("Raamat on eemaldatud")

    def naita_koik_raamatud(self):
        return self.raamatulist

    def naita_raamatud_hinna_jargi(self, raamatud):
        hindSorted = sorted(raamatud, key=lambda x: x.hind)
        print(hindSorted)

    def naita_koige_populaarsem_raamat(self, raamatud):
        reitingSorted = sorted(raamatud, key=lambda x: x.reiting)
        print(reitingSorted[-1])

raamat1 = Raamat("kukeke1", 2, 6, 4)
raamat2 = Raamat("kartul2", 3, 4, 5)
raamat3 = Raamat("kapsas3", 3, 4, 1)
raamatupood1 = Raamatupood("raamatupood1", 2)

raamatupood1.lisa_raamat(raamat1)
raamatupood1.lisa_raamat(raamat2)
raamatupood1.lisa_raamat(raamat3)
raamatupood1.naita_koik_raamatud()
raamatupood1.naita_raamatud_hinna_jargi(raamatupood1.raamatulist)
raamatupood1.naita_koige_populaarsem_raamat(raamatupood1.raamatulist)


