from datetime import datetime

from icecream import ic
from scipy.special import comb, perm

ic.configureOutput(prefix=lambda: datetime.now().strftime('%H:%M:%S | '),
                   includeContext=False)


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


def big_pi_start():
    molecular = comb(2, 1) * (comb(6, 1) * comb(22, 3) + comb(6, 2) *
                              comb(22, 2) + comb(6, 3) * comb(22, 1) + comb(6, 4)) + comb(2, 2)
    denominator = comb(30, 5)
    return Fraction(molecular, denominator)


if __name__ == '__main__':
    ic(big_pi_start())
    ic(0.184 + 0.184 * 0.816)
