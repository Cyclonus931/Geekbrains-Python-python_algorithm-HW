# 7. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a, b, c = [float(i) for i in input("Enter the lengths of the sides of triangle  -> ").split()]
if a + b <= c or a + c <= b or b + c <= a:
    print("Triangle doesn't exist")
elif a == b == c:
    print("Equilateral triangle")
elif a != b and a != c and b != c:
    print("Versatile triangle")
else:
    print("Isosceles triangle")



