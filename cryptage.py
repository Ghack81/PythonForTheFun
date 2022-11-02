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

#-------------------------------------#
#nom programme : cryptage_leek_speak_plus.py

message_clair = input("tapez le message en clair : ")
message_code = message_clair

cle = [ ['s','5'], ['t','7'], ['g', '9'], ['h', '4'], ['u','||'], ['e','!'] ]

for elt  in cle:
    ancien =elt[0]
    nouveau = elt[1]
    message_code = message_code.replace(ancien, nouveau)

print('message codé : ' , message_code)


