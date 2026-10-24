# 3. kisi number ka sactorial find karo:

n = int(input("Number:"))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)