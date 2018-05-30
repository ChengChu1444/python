# wuerfel.py

# 100 mal würfel simulieren
# anzahl der 1er, 2er usw. ausgeben

from random import *
from array import *

eins = 0
zwei = 0
drei = 0
vier = 0
fuenf = 0
sechs = 0

anz = int(input("Geben sie die Anzahl der Wuerefelwuerfe ein "))

for i in range(0,anz):
    rng = randint(1,6)
    if(rng == 1):
        eins += 1
    if(rng == 2):
        zwei += 1
    if(rng == 3):
        drei += 1
    if(rng == 4):
        vier += 1
    if(rng == 5):
        fuenf += 1
    if(rng == 6):
        sechs += 1

print("1er",eins)
print("2er",zwei)
print("3er",drei)
print("4er",vier)
print("5er",fuenf)
print("6er",sechs)
        