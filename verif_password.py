# exemple de vérification de mot de passe
password = input("Entrer votre mot de passe : ")
# variable pour le nombre de caractère le nombre de caractère du password
password_lenght = len(password)

# vérifier si le mot de passe possède 8 caractère
if password_lenght <= 8:
 print("Mot de passe trop court !")
elif 8 < password_lenght <= 12:
 print("Mot de passe moyen !")
else:
 print("Mot de passe parfait !")

 print(password)
 print(password_lenght)