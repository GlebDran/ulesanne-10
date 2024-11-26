hind = 12.90
jootraha_protsent = 0.10
sõprade_arv = int(input("Mitu sõpra on pitsa jagamisel kokku? "))

kogusumma = hind + hind * jootraha_protsent
jagatav_summa = kogusumma / sõprade_arv
print(f"Igaüks peab maksma {jagatav_summa:.2f} €")

