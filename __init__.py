import math

DEPTH = 20
NUM_INSERT = 10 ** 3
SIZE = 10 ** 7


def calculate_probability_of_false_positive():
    prob = (
        1 - math.e ** (
            -1 * DEPTH * NUM_INSERT / SIZE
        )
    ) ** DEPTH

    return prob


if __name__ == '__main__':
    print "num hash functions: ".ljust(20) + "{depth}".format(depth=DEPTH)
    print "num inserted: ".ljust(20) + "{inserted}".format(inserted=NUM_INSERT)
    print "num 'bits': ".ljust(20) + "{size}".format(size=SIZE)
    print "{p} probability of false positive".format(
        p=calculate_probability_of_false_positive()
    )