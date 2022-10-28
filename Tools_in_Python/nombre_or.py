# -*- coding: utf-8 -*-
F = [1,1,2,3]
n = 3
while (abs(F[n-2]/F[n-3]-F[n]/F[n-1])>10**(-16)):
    u = F[n]+F[n-1]
    F.extend([u])
    n +=1
    
print(F[n]/F[n-1])
