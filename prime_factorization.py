import numpy as np

def isPrime(num):
    factor_lst = [i for i in range(2,num+1) if num % i == 0]
    return(factor_lst == [num])
    
user_input = int(input('Find Prime Factors: '))
prime_lst = []
num = user_input
if user_input == 0:
    print('___Quitting Program___')
elif user_input == 1:
    print('Error: 1 has no prime factorization.')
elif user_input < 0:
    print('Error: Enter a Positive Integer')
else:
    while np.prod(prime_lst) != user_input:
        min_prime = min([i for i in range(2,num+1) if num % i == 0 and isPrime(i)])
        prime_lst.append(min_prime)
        num = int(num/min_prime)
    print('The Prime Factorization of %d is %s' % (user_input,prime_lst))