# Split into primes

# Lets create a function that will find if a number is prime or not

def prime(num = int):     
    global value
    for index in range(1,num):
        if (num % index == 0) and (index != 1):
            value = 0
            return prime
    value = 1
    return prime

# The function belolow will create a list of prime numbers candidates for a certain number

def candidates(num = int):
    global set_of_primes
    set_of_primes = []
    for index in range(2,num + 1):
        prime(index)
        if value == 1:
            set_of_primes.append(index)
    return set_of_primes

# Will search true candidates to find wich fit and then again for a new number (num = num / index)

def split_into_primes(num = int):
    results = []
    num = num
    while (num > 1):
        candidates(num)
        for index in set_of_primes:
            if num % index == 0:
                results.append(index)
                break
        num = int(num / index)
    return results        