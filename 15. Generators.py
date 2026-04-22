
print(f"Print 10 fibonacci numbers")

def fib(n):
    a, b= 0, 1
    while n>0:
        a, b = b, a+b
        n = n-1
        yield a

for n in fib(10):
    print(n, end=" ")

print()
print("*"*50)

print(f"Print fibonacci numbers between 0 and 100")

def fib1():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for n in fib1():
    if n > 100:
        break

    print(n, end=" ")

print()
print("*"*50)