# Ariel Tynan
# Euler Problem 047, Distinct primes factors, solved in Python
# Started 4 March 2022


from numpy import sqrt



n = 1000000

valid = 0 #Number of consecutive successes
for i in range(2,n): #for all numbers tested
    numFacts = 0 #variable governing number of unique prime factors
    temp = int(i) # hold onto i for printing

    div2 = False
    while temp % 2 == 0: #Governing even numbers
        if div2 == False:
            numFacts = numFacts + 1
            div2 = True
        temp = temp/2
    for j in range(3, int(sqrt(temp)) + 2,2): #For odd numbers
        divn = False
        while temp % j == 0:
            if divn == False:
                numFacts = numFacts + 1
                divn = True
            temp = temp / j
            #print(temp)
    # Check for remainder (prime factor not equal to one)
    if temp != 1:
        numFacts = numFacts + 1

    print(i,numFacts, temp)
    if numFacts == 4: # if a number has exactly 4 distinct prime factors
        valid = valid + 1
    else:
        valid = 0

    if valid == 4: # four consecutive numbers with 4 distinct prime factors
        print(i - 3)
        break








