# -*- coding: utf-8 -*-
# Suite de Fibonacci

F =[1,1]
for n in range(30):
    F.extend([F[n+1]+ F[n]])

print(F)