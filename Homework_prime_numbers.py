# Please write a program that print the first N prime numbers.
# N should be declared as a variable at the beginning.
# You can hand it in as a link to your file at github or as a file directly.


def prime(count, n):
    for i in range(2, n-1):
        if n % i == 0:
            return count
        else:
            continue
    print(str(n))
    count += 1
    return count


print("Please, enter N. It must be an natural number:")
N = int(input())


s = 1  # number to test
times = 0  # times a prime number was found
if N <= 0:
    print("Wrong! Must be a natural number!")
else:
    print("You entered " + str(N) + '. First ' + str(N) + ' prime number/s is/are:')
    while True:
        times = prime(times, s)
        s += 1
        if times == N:
            break




