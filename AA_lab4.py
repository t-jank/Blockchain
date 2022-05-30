import math
import numpy as np
import matplotlib.pyplot as plt
import random

q = 0.2
p = 1-q
n = 5 # liczba potwierdzen (nadbudowan blokow) potrzebnych by uznac transakcje za potwierdzona
k = 2 # ile adwersarz zbudowal, gdy uczciwy zbudowal n, k<n

def Newton(a,b):
    return math.factorial(a) / (math.factorial(b) * math.factorial(a-b))
'''
####### podpunkt a1 #######
n = 12 # 1,3,6,12,24,48
for q in np.arange(0.02, 0.5, 0.02):
    lamdba = n*q/p
    sumnak = 0
    sumgrun = 0
    for k in range(0,n-1):
        sumnak += math.exp(-lamdba)*(lamdba**k)/math.factorial(k)*(1-q)
        sumgrun += (p**n * q**k - q**n * p**k) * Newton(k+n-1,k)
    PNakamoto = 1 - sumnak
    P = (q/p)**(n-k)
    PGrunspan = 1 - sumgrun
    plt.plot(q,PNakamoto, color='b', marker='.', label='Nakamoto' if q == 0.02 else "")
    plt.plot(q,PGrunspan, color='g', marker='.', label='Grunspan' if q == 0.02 else "")
    plt.plot(q,P, color='orange', marker='.', label='P' if q == 0.02 else "")
plt.xlabel('q')
plt.ylabel('P')
plt.title('P')

plt.legend()
plt.show()
'''

########## podpunkt b ###########

def symulator_ataku(n,q):
    adw_counter=0
    ucz_counter=0 # liczba wykopanych blokow przez adwersarza i uczwiwe wezly
    while ucz_counter < n:
        x = random.random()
        if x <= q:
            adw_counter += 1
        else:
            ucz_counter += 1
    while ucz_counter - adw_counter < 100:
        if adw_counter >= ucz_counter:
            return 1 # atak sie powiodl
        x = random.random()
        if x <= q:
            adw_counter += 1
        else:
            ucz_counter += 1
    return 0 # atak sie nie powiodl

# wykres prawdop. ataku w zaleznosci od q przy ustalonym n
n = 6
for q in np.arange(0.0, 0.55, 0.02):
    counter=0
    for i in range(0,10000):
        counter += symulator_ataku(n,q)
    P_ataku = counter/100
    plt.plot(q,P_ataku, color='b', marker='.')
plt.xlabel('q')
plt.ylabel('Prawdopodobienstwo skutecznego ataku [%]')
plt.title('n = 6')
plt.show()

# wykres prawdop. ataku w zaleznosci od n przy ustalonym q
q = 0.3
for n in range(1, 11):
    counter=0
    for i in range(0,10000):
        counter += symulator_ataku(n,q)
    P_ataku = counter/100
    plt.plot(n,P_ataku, color='b', marker='.')
plt.xlabel('n')
plt.ylabel('Prawdopodobienstwo skutecznego ataku [%]')
plt.title('q = 0.3')
plt.show()

#print('n = ',n,'\nq = ',q,'\nPrawdopodobienstwo skutecznego ataku: ',P_ataku,'%.',sep='')

