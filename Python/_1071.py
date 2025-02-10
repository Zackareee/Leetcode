# 1071. Greatest Common Divisor of Strings

import pytest
from typing import List


class Solution:
    # 21 ms | Beats 5.44%
    # 18.06 MB | Beats 7.63%
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_length = min(len(str1), len(str2))
        gdc = ""
        for i in range(min_length):
            val1 = str1[0 : i + 1]
            val2 = str2[0 : i + 1]
            if (
                val1 == val2
                and "".join(str1.split(val1)) == ""
                and "".join(str2.split(val2)) == ""
            ):
                gdc = val1
        return gdc


@pytest.mark.parametrize(
    "str1, str2, expected",
    [
        ["ABCABC", "ABC", "ABC"],
        ["ABABAB", "ABAB", "AB"],
        ["LEET", "CODE", ""],
    ],
    ids=["test_case_1", "test_case_2", "test_case_3"],
)
def test_cases(str1: str, str2: str, expected: str):
    val = Solution()

    result: str = val.gcdOfStrings(str1, str2)

    assert result == expected
