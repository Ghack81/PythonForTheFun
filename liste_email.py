# Autre methode de création de liste
text = input("Entrer une chaine de la forme : (email-pseudo-motdepasse)").split("-")
 print(text)
 print("Salut {}, ton email est {}, et ton mot de passe est {}".format(text[1], text[0], text[2]))

 # for : pour une valeur de départ (1), jusqu'à une valeur d'arrivée (5)
for num_client in range(1, 6):
 print("Vous étes le client n° ", num_client)

#for each : pour chaque valeur d'une liste donnée
 print("Email envoyé à : mention.herve@gmail.com")
 print("Email envoyé à : mention@gmail.be")
 print("Email envoyé à : herve@gmail.yt")

# Lister les Emails
emails = ['mention.herve@gmail.com', 'mention@gmail.be', 'mention@yahoo.be', 'dark@proton.com', 'herve@gmail.yt']

# blacklist
blacklist = ['mention@yahoo.be', 'dark@proton.com']

# pour chaqu'une des valeurs, j'affiche "Email envoyé à [INSERER l'Email]"
# pour chaque email depuis ma liste d'email
for email in emails :

    if email in blacklist :
        print("Email {} interdit ! Envoi impossible...".format(email))
        continue

    print("Email envoyé à :", email)