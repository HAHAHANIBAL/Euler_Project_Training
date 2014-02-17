
from pylab import *

def primelist(limit):
    crosslimit=int(sqrt(limit))
    sieve=[False]*(limit+1)
    for i in xrange(4,limit+1,2):
        sieve[i]=True

    for i in xrange(3,crosslimit+1,2):
        if not sieve[i]:
            #cross out all the odd m multipliers
            for m in xrange(i*i,limit+1,2*i):
                sieve[m]=True

    prime=[]
    for i in range(2,limit+1):
        if not sieve[i]:
            prime.append(i)

    return prime


prime=primelist(10000)


#generate possible primes without even numbers or 5s in the digits
possible_prime=[]
for i in range(0,len(prime)):
    number=prime[i]
    while number:
        if prime[i]>10 and (number%10)%2==0:
            break
        elif prime[i]>10 and (number%10)%5==0:
            break
        number/=10
    if number==0:
        possible_prime.append(prime[i])


#rotation to find the circular prime
circular_prime=[]

for i in range(0,len(possible_prime)):
    number=possible_prime[i]
    number_str=str(number)
    if number<10:
        circular_prime.append(number)
    elif number>10 and number<100:
        if int(number_str[1]+number_str[0]) in possible_prime:
            circular_prime.append(number)
    elif number>100 and number<1000:
        if int(number_str[2]+number_str[0]+number_str[1]) in possible_prime and int(number_str[1]+number_str[2]+number_str[0]) in possible_prime:
            circular_prime.append(number)
    else:
        if int(number_str[1]+number_str[2]+number_str[3]+number_str[0]) in possible_prime and \
                        int(number_str[2]+number_str[3]+number_str[0]+number_str[1]) in possible_prime and \
                        int(number_str[3]+number_str[0]+number_str[1]+number_str[2]) in possible_prime:
            circular_prime.append(number)

print circular_prime
print len(circular_prime)