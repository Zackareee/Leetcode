# 2390. Removing Stars From a String

import pytest
from typing import List


class Solution:
    # 3 ms | Beats 94.62%
    # 18.52 MB | Beats 56.46%

    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(i.bit_count())
        return result


@pytest.mark.parametrize(
    "inp, expected",
    [
        [2, [0, 1, 1]],
        [5, [0, 1, 1, 2, 1, 2]],
    ],
    ids=["test_case_1", "test_case_2"],
)
def test_cases(inp: str, expected: str):
    val = Solution()

    result: str = val.countBits(inp)

    assert result == expected
