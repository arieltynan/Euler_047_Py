# Ariel Tynan
# Euler Problem 047, Distinct primes factors, solved in Python
# Started 4 March 2022

def prime_Sieve(n): #Function modified from Geeksforgeeks, used in Euler_046_Py
     
    primes = [] # initial empty list of primes
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            primes.append(p)
    return primes


n = 200000
pList = prime_Sieve(n) #Creates list of primes under x

valid = 0 #Number of consecutive successes
for i in range(100000,n): #for all numbers tested
    numFacts = 0 #variable governing number of unique prime factors
    temp = 0
    while temp != 1: # when temp = 1, all factors have been removed
        temp = i
        for j in range(0,len(pList)): #list of primes
            sameFact = False # if same fact, do not count again
            if numFacts > 4:
                temp = 1 # breaks out of loop if more than 4 distinct prime factors
            while temp % pList[j] == 0: #divides out all instances of each prime factor, i.e. 32 -> 2 instead of 16
                temp = temp/pList[j]
                if sameFact == False:
                    numFacts = numFacts + 1
                    sameFact = True
                
        print(i,numFacts, temp)
        if numFacts == 4: # if a number has exactly 4 distinct prime factors
            valid = valid + 1
        else:
            valid = 0
    if valid == 4: # four consecutive numbers with 4 distinct prime factors
        print(i - 3)
        break








