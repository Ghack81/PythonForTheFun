# code

# wallet = 5000
# computer_price = 50000

# le prix de l'ordinateur est inférieur à 1000€
# print(computer_price <= wallet)  # boolean True / False
#  if wallet <= computer_price or computer_price > 1000:
# print("L'achat est possible !")
# wallet = wallet - computer_price (écriture simplifier)
# wallet -= computer_price
# afficher le wallet après l'achat
# else:
# print("L'achat est impossible, vous n'avez que " + str(wallet) + "€")
# ou
# print("L'achat est impossible, vous n'avez que {}€".format(wallet))

# text = ("L'achat est possible !", "L'achet est implossible !")[computer_price <= 1000]
# print(text)

# print(wallet)

# exemple de vérification de mot de passe
# password = input("Entrer votre mot de passe : ")
# variable pour le nombre de caractère le nombre de caractère du password
# password_lenght = len(password)

# vérifier si le mot de passe possède 8 caractère
# if password_lenght <= 8:
# print("Mot de passe trop court !")
# elif 8 < password_lenght <= 12:
# print("Mot de passe moyen !")
# else:
# print("Mot de passe parfait !")

# print(password)
# print(password_lenght)

# place de cinéma
# récolter l'age de la personne "Quel est votre âge ?"
# si la personne est mineur -> 7€
# si la personne est majeur -> 12€
# souhaitez vous du popcorn ?
# si oui -> +5€
# afficher ce prix total à payer

# age_mineur = 7
# age_majeur = 12
# popcorn = 5

# client1 = str(input("Quel est votre âge ? "))
# print("Le client est agé de " + str(client1) + " ans !")

# if client1 == 18:
# print("Le prix pour un client de " + str(client1) + " ans est de 7€ !")
# else:
# print("Le prix pour un client de " + str(client1) + " ans est de 12€ !)")

# les listes
# creer une liste qui va stocker des pseudo pour un jeu en ligne
import statistics
from random import shuffle

online_player = ["Tom", "Steve", "Pierre", "Bob"]
# print(online_player)
# print(online_player[0])
# recuperer le dernier element de la liste
# print(online_player[len(online_player) -1])
# Modifier la valeur "Tom" par un autre pseudo
online_player[0] = "Clemax"
print(online_player[0])
# injecter une valeur entre "Steve et Pierre"
# la fonction  .insert permet l'insertion dans la liste
# la fonction  .insert permet l'insertion dans la listeonline_player.insert(2, "BernardGamer")
print(online_player)
# la fonction  .insert permet l'insertion dans la listeprint(online_player[2])
# la fonction  .insert permet l'insertion dans la listeonline_player.insert(5, "KillerGamer")
# print(online_player)
# autre méthode de changement de valeur dans une liste
# la fonction  .insert permet l'insertion dans la listeonline_player[1:6] = ["WarMax", "NitroGame"]
# la fonction  .insert permet l'insertion dans la listeprint(online_player)
# en ajouter d'autres
# on imagine qu'un joueur "Bob" se connecte
online_player.append("StudentGame")
print(online_player)
# autre méthode
online_player.extend(["GameOfTrone", "BlackHack"])
print(online_player)
# exemple du joueur Bob se deconnecte
del online_player[3]
# autre méthode
online_player.pop(3)
print(online_player)
# autre méthode "retirer par le nom"
online_player.remove("Pierre")
print(online_player)
# Exemple pour supprimer toute la liste
# del online_player[:] # trop redonden / vieux
online_player.clear()
print(online_player)

# Exemple de calcule de moyenne
notes = [
    8, 12, 16,
    9, 4, 15,
    14, 16
]
print(notes)
shuffle(notes)
print(notes)
# module : statistics avec "mean" -> moyen qui peut être importer
# de 'from statistic import mean' en retirant statistic dans "result"
result = statistics.mean(notes)
print("La moyenne des éléves est de {}".format(result))
# autre methode de création de liste
# text = input("Entrer une chaine de la forme : (email-pseudo-motdepasse)").split("-")
# print(text)
# print("Salut {}, ton email est {}, et ton mot de passe est {}".format(text[1], text[0], text[2]))

# for : pour une valeur de départ (1), jusqu'à une valeur d'arrivée (5)
# for num_client in range(1, 6):
# print("Vous étes le client n° ", num_client)

# for each : pour chaque valeur d'une liste donnée
# print("Email envoyé à : test-name@gmail.com")
# print("Email envoyé à : first-namen@gmail.com")
# print("Email envoyé à : tom@gmail.com")

# Lister les Emails
emails = ['tom@gmail.com', 'test-name@gmail.be', 'first-name@yahoo.be', 'dark@proton.com', 'second-mail@gmail.com']

# blacklist
blacklist = ['paul@yahoo.be', 'dark@proton.com']

# pour chaqu'une des valeurs, j'affiche "Email envoyé à [INSERER l'Email]"
# pour chaque email depuis ma liste d'email
for email in emails :

    if email in blacklist :
        print("Email {} interdit ! Envoi impossible...".format(email))
        continue

    print("Email envoyé à :", email)

# while : tant qu'une condition est vrai
# salarié 1500 / mois
salary = 1500

# tant que salaire < 2000€, +120€
while salary < 20000 :
    # ajouter 120€ au salaire
    salary += 120
    # Afficher le résultat
    print("Votre salaire actuel est de ", salary, "€")
print("Fin du programme !")

# un youtubeur "Graven", 2500 abonnés
suscribers_count = 2500

# il gagne 10% d'audience supplementaire par mois
months = 0

# on souhaite estimer, combien aurat'il d'abonnés, après 2 ans (24 mois)
while months <= 24 :
    # augmentation d'audience
    # +30% : 1 +(30/100) : 1.3
    # -20% : 1 -(20/100) : 0.8
    # +10% : 1 +(10/100) : 1.1
    suscribers_count *= 1.10

    # afficher le nombre d'abonnés
    print("Vous avez actuellement {} d'abonnés !".format(suscribers_count))

    # on passe au mois suivant
    months += 1


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

# fonction
def welcome():
    # instruction appartenant à welcome()
    print("Bienvenue sur ma chaine Youtube")
    result = 5 + 6
    print("Le résultat du calcul est ", result)


welcome()
