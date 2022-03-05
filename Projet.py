# prix des pops corns
price_pop = 5
# prix des tickets
price_ticket = 12
# Demande la somme du porte-feuille
wallet = int(input("Combien avez vous dans votre porte-feuille ?"))
print ("Vous avez " + str(wallet) + "€ dans votre porte-feuille")
# demandez l'age de la personne
age = int(input("Quel est votre age ?"))
print ("Vous avez " + str(age) + " ans !")

# Si age personne < 18ans --> 7€
if age < 18:
    price_ticket = 7
    print ("Le prix de votre ticket est de " + str(price_ticket) + "€")
# si age personne > 18 --> 12€
elif age >= 18:
    print ("Le prix de votre ticket est donc de " + str(price_ticket) + "€") 
# demander à la personne si elle veut pop corn
pop_corn = input ("Voulez vous des pops-corns ? (Oui, Non)")
# si réponse Oui --> affiche le prix pops corns
if pop_corn == "Oui":
    print ("Le prix est de " + str(price_pop) + "€")
    print ("Cela vous couteras " + str(price_pop + price_ticket) + "€")
# Si réponse Non --> n'affiche pas le prix
elif pop_corn == "Non":
    print ("Cela vous couteras " + str(price_ticket) + "€")

# demande si la personne veut payer
request = input("Voulez vous payez ? (Oui, Non)")
# Variable pour savoir le totale du prix à payer
total_price = price_pop + price_ticket
total_ticket = price_ticket

# si la réponse est Oui et qu'il a assez d'argent alors le calcul se fait
if request == "Oui" and pop_corn == "Oui" and price_ticket + price_pop <= wallet:
    print ("Il vous resteras " + str(wallet - total_price) + "€ dans votre porte-feuille")
# Si réponse Oui et que pop corn -> Non et qu'il a assez d'argent alors le calcul se fait
elif request == "Oui" and pop_corn == "Non" and price_ticket <= wallet:
    print ("Il vous resteras donc " + str(wallet - total_ticket) + "€ dans votre porte-feuille")
# Si réponse Oui et que total prix et total ticket est supérieur a porte-feuille alors pas payer
elif request == "Oui" and total_price > wallet and total_ticket > wallet:
    print ("Désoler vous n'avez pas assez d'argent pour payer donc je peut pas vous faire entrer !")
# si réponse Non -> peut pas rentrer
elif request == "Non":
    print ("Vous ne pouvez donc pas rentrer !")

print ("Fin de programme !")

