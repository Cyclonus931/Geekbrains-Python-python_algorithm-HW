# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import cProfile as cp
import math

n = 800


def loop(a):
    num = 2
    i = 0
    while i != a:
        num = num * math.sqrt(num)
        i += 1
    print(f'After {a} iterations the result is {num} (Loop)')


cp.run('loop(n)')

print('########################################################################')


# After 800 iterations the result is inf (Loop)
#          805 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 main.py:11(loop)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       800    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def recursion(i, num, a):
    if i == a:
        print(f'After {i} iterations the result is {num} (Recursion)')
        return num
    elif i <= a:
        return recursion(i + 1, num * math.sqrt(num), a)


cp.run('recursion(0, 2, n)')

# After 800 iterations the result is inf (Recursion)
#          1605 function calls (805 primitive calls) in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#     801/1    0.002    0.000    0.002    0.002 main.py:20(recursion)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       800    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
