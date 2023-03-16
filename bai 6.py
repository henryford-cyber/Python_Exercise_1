import math
x = int(input("Enter x = "))
print(math.factorial(x))


def nam_tan_nguyen(x):
    exp = 0.0001
    first = x
    mu = 5
    step = 1
    second = first - (x**3/math.factorial(3))
    while (abs(first-second) > exp):
        first = second
        if (step % 2 == 0):
            second = first-(x**mu/math.factorial(mu))
            print(mu)
            print("-")
            step = step+1
            mu = mu+2

        else:
            second = first+(x**mu/math.factorial(mu))
            print(mu)
            print("+")
            step = step+1
            mu = mu+2

    return first


print("Solution :", nam_tan_nguyen(x))
