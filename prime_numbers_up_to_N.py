
def prime(n):
    num = 0
    for i in range(2, n-1):
        if n % i == 0:
            num = + 1
        else:
            continue
    if num == 0:
        print(str(n))


print("Please, enter N. It must be an natural number:")
N = int(input())
print("You entered " + str(N) + '. First ' + str(N) + ' prime numbers are:')

for n in range(N):
    if n == 0:
        continue
    else:
        prime(n)


