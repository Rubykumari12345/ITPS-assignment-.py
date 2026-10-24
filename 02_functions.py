# 02. function se fibonacci series generate karo:

def fibonacci(n):
    a, b = 0, 1
    fib = []
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib

print(fibonacci(5))