# factorial recursive

n = int(input("Geben Sie eine Zahl ein "))

def fact(n):
    print("calc fact for",n)
    if(n==1):
        return 1
    else:
        return n * fact(n-1)

print(fact(n))