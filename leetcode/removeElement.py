#移除元素--双指针
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        j = 0
        
        while j <= i:
            if nums[j] == val:
                nums[j], nums[i] = nums[i], nums[j]
                i -= 1
            else:
                j += 1
        
        return i + 1
    
#移除元素--快慢指针
# def removeElement(self, nums: List[int], val: int) -> int:
#     slow = 0
#     for fast in range(len(nums)):
#         if nums[fast] != val:
#             nums[slow] = nums[fast]
#             slow += 1
#     return slow