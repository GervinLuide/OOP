from praks3.jaatisekiosk import JaatiseKiosk

kiosk = JaatiseKiosk("Varbavahe", "jäätist")
kiosk.jaatise_valik = "Vanilli, mandli, sokolaadi"
kiosk.kirjelda_restoran()
kiosk.naita_jaatise_valik()