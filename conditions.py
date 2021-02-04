# code

wallet = 5000
computer_price = 50000

# le prix de l'ordinateur est inférieur à 1000€
print(computer_price <= wallet)  # boolean True / False
if wallet <= computer_price or computer_price > 1000:
 print("L'achat est possible !")
 wallet = wallet - computer_price (écriture simplifier)
 wallet -= computer_price
# afficher le wallet après l'achat
 else:
 print("L'achat est impossible, vous n'avez que " + str(wallet) + "€")
# ou
 print("L'achat est impossible, vous n'avez que {}€".format(wallet))

 text = ("L'achat est possible !", "L'achet est implossible !")[computer_price <= 1000]
 print(text)

 print(wallet)