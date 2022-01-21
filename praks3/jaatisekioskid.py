from jaatisekiosk import JaatiseKiosk

kiosk = JaatiseKiosk("Minu kiosk", "jäätist")
kiosk.jaatise_valik = "Vanilli, mandli, sokolaadi"
kiosk.kirjelda_restoraan()
kiosk.naita_jaatise_valik()