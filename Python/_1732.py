# 1732. Find the Highest Altitude

import pytest
from typing import List


class Solution:
    # 0 ms | Beats 100%
    # 17.70 MB | Beats 45.10%
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        current_altitude = highest_altitude
        for i in gain:
            current_altitude += i
            if current_altitude > highest_altitude:
                highest_altitude = current_altitude
        return highest_altitude
