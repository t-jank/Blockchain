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

def Grunspan(n,q):
    p = 1-q
    sumgrun = 0
    for k in range(0,n-1):
        sumgrun += (p**n * q**k - q**n * p**k) * Newton(k+n-1,k)
    PGrunspan = 1 - sumgrun
    return PGrunspan

def Nakamoto(n,q):
    p = 1-q
    lamdba = n*q/p
    sumnak = 0
    for k in range(0,n-1):
        sumnak += math.exp(-lamdba)*(lamdba**k)/math.factorial(k)*(1-q)
    PNakamoto = 1 - sumnak
    return PNakamoto

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

####### podpunkt a1 #######
'''
n = 6 # 1,3,6,12,24,48
for q in np.arange(0, 0.51, 0.01):
    plt.plot(q,Nakamoto(n,q), color='orange', marker='.', label='Nakamoto' if q == 0 else "")
    plt.plot(q,Grunspan(n,q), color='g', marker='.', label='Grunspan' if q == 0 else "")
    #plt.plot(q,P, color='b', marker='.', label='P' if q == 0.02 else "")
plt.xlabel('q')
plt.ylabel('P')
plt.title('Porownanie analiz ataku double spending, n='+str(n))
plt.legend()
plt.show()
'''
########## podpunkt b ###########
# wykres prawdop. ataku w zaleznosci od q przy ustalonym n
n = 6
for q in np.arange(0, 0.51, 0.01):
    counter=0
    for i in range(0,10000):
        counter += symulator_ataku(n,q)
    P_ataku = counter/100
    plt.plot(q,P_ataku, color='blue', marker='.', label='symulacja' if q == 0 else "")
    plt.plot(q,Nakamoto(n,q)*100, color='orangered', marker='.', label='Nakamoto' if q == 0 else "")
    plt.plot(q,Grunspan(n,q)*100, color='springgreen', marker='.', label='Grunspan' if q == 0 else "")
plt.xlabel('q')
plt.ylabel('Prawdopodobienstwo skutecznego ataku [%]')
plt.title('n = '+str(n))
plt.legend()
plt.show()

'''
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
plt.title('Symulator ataku "double spending": wykres P(n), q = '+str(q))
plt.ylim([0,100])
plt.show()
'''
#print('n = ',n,'\nq = ',q,'\nPrawdopodobienstwo skutecznego ataku: ',P_ataku,'%.',sep='')

