import sys


def birthday_probability(ydays: int, pcnt: int, drange: int):
    res = 1
    for i in range(pcnt):
        res *= (ydays - i - (2 * drange + 1)) / ydays
    return 1 - res


if __name__ == '__main__':
    print(birthday_probability(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
