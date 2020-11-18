# Please write a program that print the first N prime numbers.
# N should be declared as a variable at the beginning.
# You can hand it in as a link to your file at github or as a file directly.

#
# def prime_numbers(n):
#         for i in range(2, n-1):
#             if n % i == 0:
#                 False
#                 break
#             else:
#
# print(prime_numbers(45))


def prime(n):
   for i in range(2, n-1):
       if n % i == 0:
           break
       else:
           print(str(n))
           break



print("Please, enter N:")
N = int(input())
print("You entered " + str(N) + '. First ' + str(N) + ' prime numbers are:')

for n in range(N):
    if n == 0:
        continue
    if n == 1:
        print('1')
    if n == 2:
        continue
    if n ==3:
        print('3')
    else:
        prime(n)




#
# N = 12
# num = 1
# counter = 0
#
#
# def modulo_times(number, count_primes):
#     k = 1
#     mod_times = 0
#     for i in range(number):
#         if number == 1:
#             mod_times = 2
#             print('hi!')
#             break
#         if number % i == 0:
#             mod_times = + 1
#             print('hi again!')
#     if mod_times == 2:
#         print(str(number) + ' is prime')
#         count_primes = + 1
#         return count_primes
#
#
# while True:
#     counter = modulo_times(num, counter)
#     num = + 1
#     if N == counter:
#         break
#

