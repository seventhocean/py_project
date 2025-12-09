##哈希表
from collections import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        for num,cnt in counts.items():
            if cnt > n // 2:
                return num
            
##Boyer-Moore 投票算法
def majorityElement(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
