import math


def sin(theta):
    # make points outside of [0, 2pi] equal to inside the range of sin(x) because it is periodic
    theta = math.fmod(theta + math.pi, 2 * math.pi) - math.pi
    result = 0
    # initial values
    termsign = 1
    power = 1

    for x in range(10):
        result += (math.pow(theta, power) / math.factorial(power)) * termsign
        termsign *= -1
        power += 2

    return result


def cos(theta):
    # make points outside of [0, 2pi] equal to inside the range of sin(x) because it is periodic
    theta = math.fmod(theta + math.pi, 2 * math.pi) - math.pi
    result = 0
    # initial values
    termsign = 1
    power = 0

    for x in range(10):
        result += (math.pow(theta, power) / math.factorial(power)) * termsign
        termsign *= -1
        power += 2

    return result


def tan(theta):
    return sin(theta) / cos(theta)

# example function


def f(x):
    return - 10*x - 2*x**2
    # return 9 - x*(x-10)

# first order derivative of example function


def fprime(x):
    return 10 - 4*x
    # return -2*x + 10

# find the root closest to value


def newtonsMethod(value):
    num = value

    for x in range(100):
        nextNum = num - f(num)/fprime(num)
        num = nextNum

    return num


print(sin(2))
print(math.sin(2))
print(cos(2))
print(math.cos(2))
print(tan(2))
print(math.tan(2))
print(newtonsMethod(10.0))
print(newtonsMethod(-10.0))
