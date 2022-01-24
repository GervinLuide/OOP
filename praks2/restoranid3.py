from praks2.restoraan3 import Restoraan

resto = Restoraan("Varbavahe", "seljankat")
resto.kirjelda_restoran()
resto.ava_restoran()

resto.maara_teenindatud_kylalised(10)
print("Teenindatud ", resto.teenindatud_kylastajad, "külalist")
resto.suurenda_teenindatud_kylalised(10)
print("Päeva jooksul on teenindatud ", resto.teenindatud_kylastajad, "külalist")