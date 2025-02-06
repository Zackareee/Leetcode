# 345. Reverse Vowels of a String
import pytest


class Solution:
    VOWELS = ["a", "e", "i", "o", "u"]

    # 891 ms | Beats 5.02%
    # 18.78 MB | Beats 29.27%
    def reverseVowels(self, s: str) -> str:
        vowels_in_string: list[str] = [
            char for char in s if char.lower() in self.VOWELS
        ]
        vowels_in_string.reverse()
        new_string = ""
        for char in s:
            if char.lower() in self.VOWELS:
                char = vowels_in_string[0]  # list index out of range here.
                vowels_in_string = vowels_in_string[1:]
            new_string += char
        return new_string


@pytest.mark.parametrize(
    "_input, expected",
    [["IceCreAm", "AceCreIm"], ["leetcode", "leotcede"]],
    ids=["test_case_1", "test_case_2"],
)
def test_cases(_input: str, expected: str):
    val = Solution()

    result: str = val.reverseVowels(_input)

    assert result == expected
