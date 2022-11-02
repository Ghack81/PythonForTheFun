#cryptage d'un message basé sur le code ASCII
#nom programme : cryptage_ascii.py
message_clair =input("tapez un message à crypter : ")
message_crypte =""
longueur = len(message_clair)
for i in range(longueur):
    lettre= message_clair[i]
    codage = str(ord(lettre))
    message_crypte = message_crypte + codage 
print ("message cryptée à envoyer")
print(message_crypte)
