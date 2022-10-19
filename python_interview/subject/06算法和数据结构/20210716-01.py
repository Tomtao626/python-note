"""
二分查找
"""
from typing import List


class Solution:
    def Search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


    """
        # 变形
        # 左闭右开
        # 左开右闭
        # nums=[2,3,4,6,8,9] target=2
        left=0 right=6-1=5 mid=4
        2>4?:false  
    """
    def SearchDemo(self, nums: List[int], target: int):
        left = 0
        right = len(nums)-1
        while right < left:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
