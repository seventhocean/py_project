#合并两个有序数组
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end_m = m - 1
        end_n = n - 1
        end_k = m + n -1

        while end_m >= 0 and end_n >= 0:
            if nums1[end_m] > nums2[end_n]:
                nums1[end_k] = nums1[end_m]
                end_m = end_m -1

            else:
                nums1[end_k] = nums2[end_n]
                end_n = end_n -1 
            end_k = end_k - 1

        while end_n >= 0:
            nums1[end_k] = nums2[end_n]
            end_n = end_n - 1
            end_k = end_k - 1
def add_test():
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1,m,nums2,n)

if __name__ == "__main__":
    add_test()
