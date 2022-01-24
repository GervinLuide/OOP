class Restoraan():
    def __init__(self, res_nimi, s_tuup):
        self.restorani_nimi = res_nimi
        self.soogi_tuup = s_tuup

    teenindatud_kylastajad = 0

    def maara_teenindatud_kylalised(self, kulastajate_arv):
        self.teenindatud_kylastajad = kulastajate_arv

    def suurenda_teenindatud_kylalised(self, suurenda_kulastajate_arv):
        self.teenindatud_kylastajad += suurenda_kulastajate_arv

    def kirjelda_restoran(self):
        print("Restoran " + self.restorani_nimi + " pakub " + self.soogi_tuup)

    def ava_restoran(self):
        print("Restoran on avatud!")