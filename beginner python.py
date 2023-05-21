import random
i = True

while i:
    tal = input("Gissa ett nummer mellan 1-6 ")

    resultat = int(tal) == random.randint(1, 6)
    print (resultat)
    cont = input("Vill du fortsätta? ")
    if cont == "Nej" or "nej":
        i = False

    
