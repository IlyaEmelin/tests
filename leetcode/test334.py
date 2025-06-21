from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = 5_000_000_000
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False