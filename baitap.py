import math
import array as arr

x = 0.5
def solution_1(x):
    mu = 2;
    eps = 0.0001
    first = 1
    second = first + (x / math.factorial(1))
    while (abs(first - second) > eps):
        first = second
        second = first + (x ** mu / math.factorial(mu))
        mu = mu + 1
    return first


print("solution 1 : ", solution_1(x))
print("result 1 : ", math.e ** x)


def solution_2(x):
    mu = 2;
    eps = 0.0001
    first = 1
    plusOrMinus = 3
    second = first - (2 * 3 / 2) * x
    while (abs(first - second) > eps):
        first = second
        if (plusOrMinus % 2 != 0):
            second = first + (plusOrMinus * (plusOrMinus + 1) / 2) * (x ** mu)
        else:
            second = first - (plusOrMinus * (plusOrMinus + 1) / 2) * (x ** mu)
        mu = mu + 1
        plusOrMinus = plusOrMinus + 1
    return first


print("solution 2 : ", solution_2(x))
print("result 2 : ", 1 / ((1 + x) ** 3))


def solution_3(x):
    mu = 3;
    eps = 0.0001
    first = -x
    second = first - (x ** 2 / 2)
    while (abs(first - second) > eps):
        first = second
        second = first - (x ** mu / mu)
        mu = mu + 1
    return first


print("solution 3 : ", solution_3(x))
print("result 3 : ", math.log(1 - x))


def solution_4(x):
    mu = 2;
    eps = 0.0001
    first = 1
    second = first + ((1 / 2) * x)
    sumchan = 2
    sumle = 1
    biendemle = 1
    biendemchan = 4
    while (abs(first - second) > eps):
        first = second
        sumle = sumle * biendemle
        sumchan = sumchan * biendemchan
        if (mu % 2 == 0):
            second = first - ((sumle / sumchan) * (x ** mu))
        else:
            second = first + ((sumle / sumchan) * (x ** mu))
        mu = mu + 1
        biendemchan = biendemchan + 2
        biendemle = biendemle + 2
    return first


print("solution 4 : ", solution_4(x))
print("result 4 : ", math.sqrt(1 + x))


def solution_5(x):
    mu = 2;
    eps = 0.0001
    first = 1
    second = first - ((1 / 2) * x)
    sumchan = 2
    sumle = 1
    biendemle = 3
    biendemchan = 4
    while (abs(first - second) > eps):
        first = second
        sumle = sumle * biendemle
        sumchan = sumchan * biendemchan
        if (mu % 2 == 0):
            second = first + ((sumle / sumchan) * (x ** mu))
        else:
            second = first - ((sumle / sumchan) * (x ** mu))
        mu = mu + 1
        biendemchan = biendemchan + 2
        biendemle = biendemle + 2
    return first


print("solution 5 : ", solution_5(x))
print("result 5 : ", 1 / (math.sqrt(1 + x)))


def solution_6(x):
    mu = 5;
    eps = 0.0001
    first = x
    second = first - (x ** 3 / math.factorial(3))
    while (abs(first - second) > eps):
        first = second
        if (mu % 2 == 1):
            second = first + (x ** mu / math.factorial(mu))
        else:
            second = first - (x ** mu / math.factorial(mu))
        mu = mu + 2
    return first


print("solution 6 : ", solution_6(x))
print("result 6 : ", math.sin(x))


def solution_7(x):
    mu = 4;
    eps = 0.0001
    first = 1
    second = first - (x ** 2 / math.factorial(2))
    while (abs(first - second) > eps):
        first = second
        if (mu % 2 == 0):
            second = first + (x ** mu / math.factorial(mu))
        else:
            second = first - (x ** mu / math.factorial(mu))
        mu = mu + 2
    return first


print("solution 7 : ", solution_7(x))
print("result 7 : ", math.cos(x))


# def solution_8(x):
#     mu=3
#     eps = 0.0001
#     step=1
#     first = x
#     second = first+1/2
#
#     sumchan = 2
#     sumle = 1
#     biendemle = 3
#     biendemchan = 4
#     while(mu<20) :
#         first = second
#         if(step % 2 == 1):
#             second=first*(x**mu/mu)
#             mu = mu + 2
#         else:
#             sumle = sumle * biendemle
#             sumchan = sumchan * biendemchan
#
#             second=first+sumle/sumchan
#             biendemchan = biendemchan + 2
#             biendemle = biendemle + 2
#         step=step+1
#     return first
# print("solution 8 : ",solution_8(x))
# print("result 8 : ",math.asin(x))

def solution_9(x):
    mu = 4;
    eps = 0.0001
    first = 1
    second = first - (x ** 2 / math.factorial(3))
    while (abs(first - second) > eps):
        first = second
        if (mu % 2 == 0):
            second = first + (x ** mu / math.factorial(mu + 1))
        else:
            second = first - (x ** mu / math.factorial(mu + 1))
        mu = mu + 2
    return first


print("solution 9 : ", solution_9(x))
print("result 9 : ", (math.sin(x) / x))


def solution_10(x):
    mu = 5;
    eps = 0.0001
    first = x
    second = first - (x ** 3 / 3)
    while (abs(first - second) > eps):
        first = second
        if (mu % 2 == 1):
            second = first + (x ** mu / mu)
        else:
            second = first - (x ** mu / mu)
        mu = mu + 2
    return first


print("solution 10 : ", solution_10(x))
print("result 10 : ", math.atan(x))


def solution_11(x):
    mu = 3;
    eps = 0.0001
    first = x
    second = first - (x ** 2 / 2)
    while (abs(first - second) > eps):
        first = second
        if (mu % 2 == 1):
            second = first + (x ** mu / mu)
        else:
            second = first - (x ** mu / mu)
        mu = mu + 1
    return first


print("solution 11 : ", solution_11(x))
print("result 11 : ", math.log(1 + x))


def solution_12(x):
    mu = 5;
    eps = 0.0001
    first = 2 * x
    second = first + ((x ** 3 / 3) * 2)
    while (abs(first - second) > eps):
        first = second
        second = first + (x ** mu / mu) * 2
        mu = mu + 2
    return first


print("solution 12 : ", solution_12(x))
print("result 12 : ", math.log((1 + x) / (1 - x)))


def solution_13_1(x):
    result = ((solution_1(x)) - (1 / solution_1(x))) / 2
    return result


print("solution 13_1 : ", solution_13_1(x))
print("result 13_1 : ", math.sinh(x))


def solution_13_2(x):
    mu = 5;
    eps = 0.0001
    first = x
    second = first + (x ** 3 / math.factorial(3))
    while (abs(first - second) > eps):
        first = second
        second = first + (x ** mu / math.factorial(mu))
        mu = mu + 2
    return first


print("solution 13_2 : ", solution_13_2(x))
print("result 13_2 : ", math.sinh(x))


def solution_14_1(x):
    result = ((solution_1(x)) + (1 / solution_1(x))) / 2
    return result


print("solution 14_1 : ", solution_14_1(x))
print("result 14_1 : ", math.cosh(x))


def solution_14_2(x):
    mu = 4
    eps = 0.0001
    first = x
    second = first + (x ** 2 / math.factorial(2))
    while (abs(first - second) > eps):
        first = second
        second = first + x ** mu / math.factorial(mu)
        mu = mu + 2
    return first


print("solution 14_2 ? : ", solution_14_2(x))
print("result 14_2 : ", math.cosh(x))import math
import array as arr

x = 0.5
def solution_1(x):
    mu = 2;
    eps = 0.0001
    first = 1
    second = first + (x / math.factorial(1))
    while (abs(first - second) > eps):
        first = second
        second = first + (x ** mu / math.factorial(mu))
        mu = mu + 1
    return first


print("solution 1 : ", solution_1(x))
print("result 1 : ", math.e ** x)


def solution_2(x):
    mu = 2;
    eps = 0.0001
    first = 1
    plusOrMinus = 3
    second = first - (2 * 3 / 2) * x
    while (abs(first - second) > eps):
        first = second
        if (plusOrMinus % 2 != 0):
            second = first + (plusOrMinus * (plusOrMinus + 1) / 2) * (x ** mu)
        else:
            second = first - (plusOrMinus * (plusOrMinus + 1) / 2) * (x ** mu)
        mu = mu + 1
        plusOrMinus = plusOrMinus + 1
    return first


print("solution 2 : ", solution_2(x))
print("result 2 : ", 1 / ((1 + x) ** 3))


def solution_3(x):
    mu = 3;
    eps = 0.0001
    first = -x
    second = first - (x ** 2 / 2)
    while (abs(first - second) > eps):
        first = second
        second = first - (x ** mu / mu)
        mu = mu + 1
    return first


print("solution 3 : ", solution_3(x))
print("result 3 : ", math.log(1 - x))


def solution_4(x):
    mu = 2;
    eps = 0.0001
    first = 1
    second = first + ((1 / 2) * x)
    sumchan = 2
    sumle = 1
    biendemle = 1
    biendemchan = 4
    while (abs(first - second) > eps):
        first = second
        sumle = sumle * biendemle
        sumchan = sumchan * biendemchan
        if (mu % 2 == 0):
            second = first - ((sumle / sumchan) * (x ** mu))
        else:
            second = first + ((sumle / sumchan) * (x ** mu))
        mu = mu + 1
        biendemchan = biendemchan + 2
        biendemle = biendemle + 2
    return first


print("solution 4 : ", solution_4(x))
print("result 4 : ", math.sqrt(1 + x))


def solution_5(x):
    mu = 2;
    eps = 0.0001
    first = 1
    second = first - ((1 / 2) * x)
    sumchan = 2
    sumle = 1
    biendemle = 3
    biendemchan = 4
    while (abs(first - second) > eps):
        first = second
        sumle = sumle * biendemle
        sumchan = sumchan * biendemchan
        if (mu % 2 == 0):
            second = first + ((sumle / sumchan) * (x ** mu))
        else:
            second = first - ((sumle / sumchan) * (x ** mu))
        mu = mu + 1
        biendemchan = biendemchan + 2
        biendemle = biendemle + 2
    return first


print("solution 5 : ", solution_5(x))
print("result 5 : ", 1 / (math.sqrt(1 + x)))


def solution_6(x):
    mu = 5;
    eps = 0.0001
    first = x
    second = first - (x ** 3 / math.factorial(3))
    while (abs(first - second) > eps):
        first = second
        if (mu % 2 == 1):
            second = first + (x ** mu / math.factorial(mu))
        else:
            second = first - (x ** mu / math.factorial(mu))
        mu = mu + 2
    return first


print("solution 6 : ", solution_6(x))
print("result 6 : ", math.sin(x))


def solution_7(x):
    mu = 4;
    eps = 0.0001
    first = 1
    second = first - (x ** 2 / math.factorial(2))
    while (abs(first - second) > eps):
        first = second
        if (mu % 2 == 0):
            second = first + (x ** mu / math.factorial(mu))
        else:
            second = first - (x ** mu / math.factorial(mu))
        mu = mu + 2
    return first


print("solution 7 : ", solution_7(x))
print("result 7 : ", math.cos(x))


# def solution_8(x):
#     mu=3
#     eps = 0.0001
#     step=1
#     first = x
#     second = first+1/2
#
#     sumchan = 2
#     sumle = 1
#     biendemle = 3
#     biendemchan = 4
#     while(mu<20) :
#         first = second
#         if(step % 2 == 1):
#             second=first*(x**mu/mu)
#             mu = mu + 2
#         else:
#             sumle = sumle * biendemle
#             sumchan = sumchan * biendemchan
#
#             second=first+sumle/sumchan
#             biendemchan = biendemchan + 2
#             biendemle = biendemle + 2
#         step=step+1
#     return first
# print("solution 8 : ",solution_8(x))
# print("result 8 : ",math.asin(x))

def solution_9(x):
    mu = 4;
    eps = 0.0001
    first = 1
    second = first - (x ** 2 / math.factorial(3))
    while (abs(first - second) > eps):
        first = second
        if (mu % 2 == 0):
            second = first + (x ** mu / math.factorial(mu + 1))
        else:
            second = first - (x ** mu / math.factorial(mu + 1))
        mu = mu + 2
    return first


print("solution 9 : ", solution_9(x))
print("result 9 : ", (math.sin(x) / x))


def solution_10(x):
    mu = 5;
    eps = 0.0001
    first = x
    second = first - (x ** 3 / 3)
    while (abs(first - second) > eps):
        first = second
        if (mu % 2 == 1):
            second = first + (x ** mu / mu)
        else:
            second = first - (x ** mu / mu)
        mu = mu + 2
    return first


print("solution 10 : ", solution_10(x))
print("result 10 : ", math.atan(x))


def solution_11(x):
    mu = 3;
    eps = 0.0001
    first = x
    second = first - (x ** 2 / 2)
    while (abs(first - second) > eps):
        first = second
        if (mu % 2 == 1):
            second = first + (x ** mu / mu)
        else:
            second = first - (x ** mu / mu)
        mu = mu + 1
    return first


print("solution 11 : ", solution_11(x))
print("result 11 : ", math.log(1 + x))


def solution_12(x):
    mu = 5;
    eps = 0.0001
    first = 2 * x
    second = first + ((x ** 3 / 3) * 2)
    while (abs(first - second) > eps):
        first = second
        second = first + (x ** mu / mu) * 2
        mu = mu + 2
    return first


print("solution 12 : ", solution_12(x))
print("result 12 : ", math.log((1 + x) / (1 - x)))


def solution_13_1(x):
    result = ((solution_1(x)) - (1 / solution_1(x))) / 2
    return result


print("solution 13_1 : ", solution_13_1(x))
print("result 13_1 : ", math.sinh(x))


def solution_13_2(x):
    mu = 5;
    eps = 0.0001
    first = x
    second = first + (x ** 3 / math.factorial(3))
    while (abs(first - second) > eps):
        first = second
        second = first + (x ** mu / math.factorial(mu))
        mu = mu + 2
    return first


print("solution 13_2 : ", solution_13_2(x))
print("result 13_2 : ", math.sinh(x))


def solution_14_1(x):
    result = ((solution_1(x)) + (1 / solution_1(x))) / 2
    return result


print("solution 14_1 : ", solution_14_1(x))
print("result 14_1 : ", math.cosh(x))


def solution_14_2(x):
    mu = 4
    eps = 0.0001
    first = x
    second = first + (x ** 2 / math.factorial(2))
    while (abs(first - second) > eps):
        first = second
        second = first + x ** mu / math.factorial(mu)
        mu = mu + 2
    return first


print("solution 14_2 ? : ", solution_14_2(x))
print("result 14_2 : ", math.cosh(x))