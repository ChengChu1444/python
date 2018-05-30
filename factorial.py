# factorial.py

n = int(input("Geben sie eine Zahl ein "))

f = 1

for i in range(1,n+1):
    f = f * i

print(n,"! = ", f, sep="")