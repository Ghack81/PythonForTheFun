# Le jeu du juste prix
# choisir le prix gagnant
price = 777
while price in range(1, 1000):
# entrer le numero

   number = int(input("Entrer un prix"))

if number == price:

        print("C'est gagne!")
        print("Fin du jeu")
        #break
elif number > price:

        print("C'est moins!")

else: number < price

print("C'est plus!")


# Le jeu du juste prix
# choisir le prix gagnant
# price = 777
# while price in range(1, 1000):
# entrer le numero
# number = int(input("Entrer un prix"))
# if number == price:
# print("C'est gagne!")
# print("Fin du jeu")
# break
# elif number > price:
# print("C'est moins!")
# elif number < price:
# print("C'est plus!")