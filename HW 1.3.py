# По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b , проходящей через эти точки


print("Enter first point coordinates (x;y):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print("Enter second point coordinates (x;y):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))


if x1 == x2 :
    print(f'Equation of a straight line x = {x1}')
elif y1 == y2:
    print(f'Equation of a straight line y = {y1}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'Equation of a straight line passing through these points: y = {k}x + {b}')