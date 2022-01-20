from praks2.tootajad import Inimene

esimene = Inimene("Gervin", "Luide", 9)
esimene.tutvustus()
teine = Inimene("Danil", "kersontsev", 8)
teine.tutvustus()
kolmas = Inimene("Viktor", "Lumiste", 7)
kolmas.tutvustus()

if esimene.inimene_kvl < teine.inimene_kvl and esimene.inimene_kvl < kolmas.inimene_kvl:
    print(esimene.inimene_eesnimi, esimene.inimene_perenimi, "Olete vallandatud")
    del esimene
elif teine.inimene_kvl < esimene.inimene_kvl and teine.inimene_kvl < kolmas.inimene_kvl:
    print(teine.inimene_eesnimi, teine.inimene_perenimi, "Olete vallandatud")
    del teine
elif kolmas.inimene_kvl < esimene.inimene_kvl and kolmas.inimene_kvl < teine.inimene_kvl:
    print(kolmas.inimene_eesnimi, kolmas.inimene_perenimi, "Olete vallandatud")
    del kolmas

input()