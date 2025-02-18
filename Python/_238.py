# 238. Product of Array Except Self
import pytest
from typing import List
import math


class Solution:
    # 38 ms | Beats 19.49%
    # 22.80 MB | Beats 98.44%
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_calc = math.prod(nums)
        result = []
        for index, value in enumerate(nums):
            if value == 1:
                result.append(pre_calc)
            elif value == -1:
                result.append(pre_calc * -1)
            else:
                arr = nums[0:index] + nums[index + 1 :]
                result.append(math.prod(arr))
        return result


@pytest.mark.parametrize(
    "_input, expected",
    [[[-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]]],
    ids=["test_case_1"],
)
def test_cases(_input: List[int], expected: List[int]):
    val = Solution()

    result: List[int] = val.productExceptSelf(_input)

    assert result == expected
