# 2. Написать два алгоритма нахождения i-го по счёту простого числа.


import cProfile as cp
n = int(input('Enter the index of number: '))


# Без использования «Решета Эратосфена»;

def algo(n):
    primes = []
    for i in range(2, 10000):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    print(f'The number  = {primes[n - 1]} (without sieve)')


cp.run('algo(n)')

print('###########################################################')

# Enter the index of number: 920
# The number  = 7207 (without sieve)
#          1234 function calls in 0.326 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.326    0.326 <string>:1(<module>)
#         1    0.326    0.326    0.326    0.326 HW 4.2.py:10(algo)
#         1    0.000    0.000    0.326    0.326 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Используя алгоритм «Решето Эратосфена»

def sieve(n):
    primes = []
    nums = [i for i in range(2, 10000)]

    for i in nums:
        if i != 0:
            primes.append(i)
            for j in nums[i:]:
                if j % i == 0:
                    nums[j - 2] = 0
    print(f'The number = {primes[n - 1]} (sieve)')

    # The number = 7207 (sieve)
    #          1235 function calls in 0.536 seconds
    #
    #    Ordered by: standard name
    #
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.000    0.000    0.536    0.536 <string>:1(<module>)
    #         1    0.535    0.535    0.536    0.536 HW 4.2.py:28(sieve)
    #         1    0.000    0.000    0.000    0.000 HW 4.2.py:30(<listcomp>)
    #         1    0.000    0.000    0.536    0.536 {built-in method builtins.exec}
    #         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
    #      1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    #         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cp.run('sieve(n)')
