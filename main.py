n = int(input("Enter number: "))

primes = []

for i in range(2, n+1):
    check = True
    for j in range(2, i):
        if i % j == 0:
            check = False
            break
    if check:
        primes.append(i)

print("Prime numbers: ", *primes)

