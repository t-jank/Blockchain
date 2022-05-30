import math
import numpy as np
import matplotlib.pyplot as plt

q = 0.2
p = 1-q
n = 5 # liczba potwierdzen (nadbudowan blokow) potrzebnych by uznac transakcje za potwierdzona
k = 2 # ile adwersarz zbudowal, gdy uczciwy zbudowal n, k<n

def Newton(a,b):
    return math.factorial(a) / (math.factorial(b) * math.factorial(a-b))

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
    plt.scatter(q,PNakamoto, color='k', marker='.')
plt.xlabel('q')
plt.ylabel('P')
plt.title('P')
plt.show()

