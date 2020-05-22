def check_prime(inp):
    is_prime = True
    for i in range(2, inp):
        if(inp % i == 0):
            is_prime = False
    return is_prime


def get_prime_numbers_in_range(num):
    print('Getting prime numbers up to {0}'.format(num))
    primes = set()
    if(num == 1) or (num == 2):
        primes.add(2)
    else:
        for i in range(2, num):
            if(check_prime(i)):
                primes.add(i)
    print(list(primes))
    ans = input('What to continue..?(y/n)')
    if(ans == 'y' or ans == 'yes' or ans == 'Yes' or ans == 'YES'):
        get_prime_numbers_in_range(int(input('Enter number : ')))
    else:
        raise SystemExit


get_prime_numbers_in_range(int(input('Enter number : ')))
