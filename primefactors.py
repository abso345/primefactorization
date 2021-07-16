#!/usr/bin/env python
# coding: utf-8

# In[56]:


import math
import timeit

def findprimes(r1, r2):
    # lets use sieve of eratosthenes
    # Set all values to true for now.
    primes = [1]*(r2+1)
    primes[0] = 0 # 1 not prime
    trueprimes = []
    
    pindex = 1
    
    while((pindex + 1) <= r2):
        # Its a prime
        if (primes[pindex] == 1):
            # Insert primes into seperate list being returned
            # to caller.
            trueprimes.insert(0, pindex+1)
            
            # Now lets invalidate multiples of this prime in the list
            # Not following the most optimal way to invalidate.
            nonpindex = pindex + (pindex+1)
            while(nonpindex <= r2):
                primes[nonpindex] = 0
                nonpindex = nonpindex + (pindex+1)
        
        # move on to next index until we find one that is considered prime
        pindex = pindex + 1
        
    trueprimes.sort()
    return trueprimes
    
def factorprimes(primenumbers):
    primefactors = []
    
    # For each prime number lets see if it evenly
    # divides the user input.
    for x in primenumbers:
        # No remainder so lets add it to the factors list
        if (input_int % x == 0):
            primefactors.insert(0, x)
    
    primefactors.sort()
    return primefactors

input_int = int(input())

print(input_int, "was input")

if input_int >= 2 and input_int <= 10000000 :
    #%timeit findprimes(1, input_int) # see how fast this is shall we.
    primenumbers = findprimes(1, input_int)
    
    for x in primenumbers:
        print(x, "is prime")
    
    #%timeit factorprimes(primenumbers) # see how fast this is shall we.

    primefactors = factorprimes(primenumbers)
    
    print(len(primenumbers), "number primes", len(primefactors), "number factors")
    
    for x in primefactors:
        print(x , "is a prime factor for", input_int)
        
elif input_int == 1:
    print ("1 is not prime")
else :
    print(input_int , "invalid value.  Try values between 1 and 10000000")
    
#10000 3.95ms for finding primes, 69.2us for factorization
#9999 input 3.93ms for finding primes, 74.5us for factorization
#1000 input 325us for finding primes, 9.04us for factorization
#100 input 27.3us for finding primes, 1.66us for factorization
#10 input 3us for finding primes, 616ns for factorization
#2 input 688ns for finding primes, 366ns for factorization
# Runs at O(n) complexity



