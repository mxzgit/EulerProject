'''


If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


'''

INT = 10
result = 0
for element in range(INT):
    if(element % 3 == 0 or element % 5 ==0 ):
        result += element


print(result)