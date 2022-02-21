from oppimine import *

teemad = Andmed("klass", "objekt", "pärilus", "polümorfism", "kapseldus" )
anna = Opetaja()
kadi = Opilane()
mati = Opilane()

kadi.opib(teemad[3])
kadi.opib(teemad[1])
mati.opib(teemad[2])

kadi.unustab()




