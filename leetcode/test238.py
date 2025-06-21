from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         left, right = [1]*(len(nums)), [1]*(len(nums))
#         last = 1
#         for i, num in enumerate(nums):
#             left[i] = last
#             last = num * last
#
#         last = 1
#         for i, num in enumerate(reversed(nums)):
#             right[len(nums)- 1 - i] = last
#             last = num * last
#
#         return [ num1 * num2 for num1, num2 in zip(left, right) ]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        last = 1
        for i, num in enumerate(nums):
            result[i] = last
            last *= num

        last = 1
        for index in range(len(nums)-1, -1, -1):
            result[index] *= last
            last *= nums[index]
        return result

if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3 , 4]))