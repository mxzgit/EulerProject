'''


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


'''
import math


number = 600851475143

def isprime(a):
    for elem in range(2,int(math.sqrt(a))+1):
        if (a % elem == 0):
            return 0

    return 1


def divisor(a):
    list_prime = []
    for elem in range(2,int(math.sqrt(a))+1):
        if (a % elem == 0 and isprime(elem)) :
            list_prime.append(elem)
            if(isprime(int(a/elem))):
                list_prime.append(int(a/elem))
    return max(list_prime)

print(divisor(number))