from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1]*(len(nums)), [1]*(len(nums))
        last = 1
        for i, num in enumerate(nums):
            left[i] = last
            last = num * last

        last = 1
        for i, num in enumerate(reversed(nums)):
            right[len(nums)- 1 - i] = last
            last = num * last

        return [ num1 * num2 for num1, num2 in zip(left, right) ]


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3 , 4]))