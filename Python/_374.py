# 374. Guess Number Higher or Lower
import pytest
from typing import List
import math


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num > 20:
        return -1
    if num < 20:
        return 1
    if num == 20:
        return 0


class Solution:
    # 34 ms | Beats 76.67%
    # 18.10 MB | Beats 6.46%
    def guessNumber(self, n: int) -> int:
        min_num = 1
        max_num = n
        val = math.ceil(max_num / 2)
        while guess(val) != 0:
            up_down = guess(val)
            if up_down == -1:
                max_num = val
                val = val - math.ceil(
                    (val - min_num) / 2
                )  # possibly round up for speed
            elif up_down == 1:
                min_num = val
                val = val + math.ceil((max_num - val) / 2)

        return val


@pytest.mark.parametrize(
    "_inp, expected",
    [
        [2, 2],
    ],
    ids=["test_case_4"],
)
def test_cases(_inp: int, expected: int):
    val = Solution()
    result: int = val.guessNumber(_inp)

    assert result == expected
