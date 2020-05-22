def get_factorial_by_iteration(num):
    res = 1
    for i in range(2, num+1):
        #print(i, end=' ')
        res = res * i
        #print(res, end = ' ')
    return res


def get_factorial_by_recursion(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return num * (get_factorial_by_recursion(num-1))


num = input('Enter Number :')
result_iteration = get_factorial_by_iteration(int(num))
result_recursion = get_factorial_by_recursion(int(num))
print('\nFactorial by iteration of {0} is {1}'.format(num, result_iteration))
print('\nFactorial by recursion of {0} is {1}'.format(num, result_recursion))
