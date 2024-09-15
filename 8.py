
a = int(input("Input length of side a: "))
b = int(input("Input length of side b: "))
c = int(input("Input length of side c: "))


if a == b == c:
    print("Equilateral triangle")
elif a == b or a == c or b == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")