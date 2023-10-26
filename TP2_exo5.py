nb = int(input("Entrez un nombre :"))

if nb > 0:
    print("positif")
    if nb %2 == 0:
        print('pair')
    else:
        print('impair')

elif nb == 0:
    print('vaut 0')
else:
    print('negatif')
    if nb %2 == 0:
        print('pair')
    else:
        print('impair')
