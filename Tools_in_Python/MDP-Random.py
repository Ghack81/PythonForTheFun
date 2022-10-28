import random
passlen = int(input("enter the length of password : "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!=:;,^$@#$%^&*()?"
if passlen > 180:
    print("Le mot de passe est trop long !")
else:
    print("Mot de passe valide !")
p = "".join(random.sample(s,passlen ))
print(p)