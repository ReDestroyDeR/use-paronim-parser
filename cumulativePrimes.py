def cumulative_primes(x):
    if x == 1:
        return 1
    for i in range(2, x + 1):
        if x % i == 0:
            print(i, end=" ")
            return cumulative_primes(x // i)


for i in range(5500, 5511):
    print(i, ": ", sep="", end="")
    cumulative_primes(i)
    print()
