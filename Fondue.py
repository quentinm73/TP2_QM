BASE = 4
fromage = 800
eau = 2
ail = 2
pain = 400
nbConvive = int(input('Entrez le nombre de persone(s) conviées à la fondue :'))
Fromage = fromage * nbConvive / BASE
Eau = eau * nbConvive / BASE
Ail = ail * nbConvive / BASE
Pain = pain * nbConvive / BASE

print('Pour faire une fondue fribourgeoise pour', nbConvive, ", il vous faut :")
print(f"- {Fromage} gr de fromage")
print(f"- {Eau} dl d'eau")
print(f"- {Ail} de gousse(s) d'ail")
print(f"- {Pain} gr de pain")
