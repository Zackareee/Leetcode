# 605. Can Place Flowers
import pytest
from typing import List


class Solution:
    # 18 ms | Beats 6.86%
    # 18.31 MB | Beats 12.18%
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_flowers = 0
        index = 0
        while index < len(flowerbed):
            flower = flowerbed[index]
            previous_flower = flowerbed[max(index - 1, 0)]
            next_flower = flowerbed[min(index + 1, len(flowerbed) - 1)]
            if flower != 0:
                index += 2
                continue

            if previous_flower == 0 and next_flower == 0:
                new_flowers += 1
                flowerbed[index] = 1

            index += 1

        return new_flowers >= n


@pytest.mark.parametrize(
    "_input_flowerbed, _input_n, expected",
    [
        [[0, 0, 1, 0, 0], 1, True],
    ],
    ids=["test_case_4"],
)
def test_cases(_input_flowerbed: List[int], _input_n: int, expected: bool):
    val = Solution()

    result: bool = val.canPlaceFlowers(_input_flowerbed, _input_n)

    assert result == expected
