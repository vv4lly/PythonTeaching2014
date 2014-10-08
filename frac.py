__author__ = 'mark'

''' Demonstrate import and rational class'''


def gcd(a, b):
    # Ensure that a > b, if it is not reverse a & b
    if not a > b:
        a, b = b, a

    print("Initial fraction is {}/{}".format(a, b))
    while b != 0:
        rem = a % b
        a, b = b, rem
        print(("... {}/{}".format(a, b)))

    print("GCD is {}".format(a))
    return a


def gcdr(a, b):
    '''Recursive version of GCD'''
    # print (a, b)

    if not a > b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcdr(b, a % b)


def lcm(a, b):
    my_gcd = gcd(a, b)

    print("LCM is {}".format(a * b / my_gcd))
    return (a * b / my_gcd)


def addFrac(f1, f2):
    # f1 & f2 are tuples, this function returns a tuple
    my_lcm = lcm(f1[1], f2[1])
    my_sum = (my_lcm / f1[1] * f1[0]) + (my_lcm / f2[1] * f2[0])
    return my_sum, my_lcm


def subFrac(f1, f2):
    my_lcm = lcm(f1[1], f2[1])
    diff = (my_lcm / f1[1] * f1[0]) - (my_lcm / f2[1] * f2[0])
    return diff, my_lcm


def reduce(frac):
    my_gcd = gcd(frac[0], frac[1])
    return (frac[0] / my_gcd, frac[1] / my_gcd)


if __name__ == "__main__":
    x = lcm(12, 13)
    y = gcd(12, 13)

    z = reduce((25, 50))

    print("z =", z)