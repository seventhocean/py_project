from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
# Example usage:
sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(nums, 3)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
