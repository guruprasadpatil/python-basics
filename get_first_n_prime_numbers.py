def check_prime(inp):
    is_prime = True
    for i in range(2,inp):
        if(inp % i == 0):
            is_prime = False
    return is_prime
    

def get_n_prime(num):
    print('Getting first {0} prime numbers...'.format(num))
    primes = set()
    if(num == 1) or (num == 2):
        primes.add(2)
    else:
        count = 0
        while(len(primes) < num):
            if(count > 0):
                if(count == 1) or (count == 2):
                    primes.add(2)
                elif(count > 2):
                    if(check_prime(count) == True):
                        primes.add(count)
            count = count +1
    
    print(list(primes))
    
get_n_prime(int(input('Enter number : ')))