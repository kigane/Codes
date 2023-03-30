from datetime import datetime

from icecream import ic
from scipy.special import comb, perm

ic.configureOutput(prefix=lambda: datetime.now().strftime('%H:%M:%S | '),
                   includeContext=False)

################
# 抽5张牌，看牌型
################


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Fraction:
    def __init__(self, molecular, denominator) -> None:
        self._mol = molecular
        self._den = denominator

    def __str__(self) -> str:
        m = gcd(self._mol, self._den)
        return f"{int(self._mol / m)}/{int(self._den / m)}"

    def value(self) -> float:
        return self._mol / self._den

    def __repr__(self) -> str:
        return self.__str__() + " = " + str(round(self.value(), 7))


def four_of_a_kind():
    return Fraction(comb(13, 1)*comb(1, 1)*comb(52-4, 1), comb(52, 5))


def three_of_a_kind():
    # return Fraction(comb(13, 1)*comb(4, 3)*comb(12, 2)*comb(4, 1)*comb(4, 1), comb(52, 5))
    return Fraction(comb(13, 3)*comb(3, 1)*comb(4, 3)*comb(4, 1)*comb(4, 1), comb(52, 5))


def one_pair():
    molecular = comb(13, 4) * comb(4, 1) * comb(4, 2) * \
        comb(4, 1) * comb(4, 1) * comb(4, 1)
    denominator = comb(52, 5)
    return Fraction(molecular, denominator)


def two_pair():
    molecular = comb(13, 3) * comb(3, 1) * comb(4, 1) * comb(4, 2) * comb(4, 2)
    denominator = comb(52, 5)
    return Fraction(molecular, denominator)


def full_house():
    """
    3+2
    """
    molecular = comb(13, 1) * comb(4, 3) * comb(12, 1) * comb(4, 2)
    denominator = comb(52, 5)
    return Fraction(molecular, denominator)


def flush_and_straight_flush():
    molecular = comb(4, 1) * comb(13, 5)
    denominator = comb(52, 5)
    return Fraction(molecular, denominator)


def straight__and_straight_flush():
    molecular = 10 * (4 ** 5)  # 10种允许的序列，完全不考虑花色
    denominator = comb(52, 5)
    return Fraction(molecular, denominator)


def flush():
    """
    同花不顺
    """
    molecular = comb(4, 1) * comb(13, 5) - 40
    denominator = comb(52, 5)
    return Fraction(molecular, denominator)


def straight():
    """
    顺子，不同花
    """
    molecular = 10 * (4 ** 5) - 40
    denominator = comb(52, 5)
    return Fraction(molecular, denominator)


def straight_flush():
    """
    同花顺。
    十种序列，4种花色
    """
    return Fraction(40, comb(52, 5))


if __name__ == '__main__':
    ic(four_of_a_kind())
    ic(three_of_a_kind())
    ic(two_pair())
    ic(one_pair())
    ic(full_house())
    ic(flush_and_straight_flush())
    ic(straight__and_straight_flush())
    ic(flush())
    ic(straight())
    ic(straight_flush())
