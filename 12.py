def find_median(a, b, c):
    numbers = [a, b, c]

    numbers.sort()

    return numbers[1]

a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))

median = find_median(a, b, c)
print(f"The median is {median:.1f}")