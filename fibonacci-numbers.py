# fibonacci-numbers

n = int(input("Geben sie eine Zahl ein "))

f = 0
fletzte = 1
fvletzte = 0

print("Fibonacci Zahlen:")
print(1,end=" ")
for i in range(0, n):
    f = fletzte + fvletzte
    fvletzte = fletzte
    fletzte = f
    print(f,end=" ")
print()
