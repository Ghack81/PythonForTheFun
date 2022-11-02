#Grâce à cette table le destinaire du message pourra le décrypter.
#Pour simplifier on suppose que les caractères employés dans le message en clair sont uniquement :
#les lettres minuscules (a ... z)
#les chiffres arabes de (0 ... 9)
#l'espace pour séparer deux mot
#nom programme : table_substitution.py
# production table qui permet de traduire un message crypté en ascii

alphabet ="abcdefghijklmopqrstuvwxyz 0123456789"
longueur = len(alphabet)
print('nombre de caractères :' , longueur)
table =""
print ("table de substitution")
for i in range(longueur):
   caractere = alphabet[i] 	#récupérer le caractère correspondant à i dans la chaine 'alphabet'
   code = ord(caractere) 		#code ascii de ce caractère
   cle = str(code) + " = " + caractere +" ; " 	#clé de décryptage
   table =table +cle	#mise à jour table
print (table)
