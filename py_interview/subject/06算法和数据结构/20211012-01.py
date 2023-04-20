"""
list = [5,3,4,7,9,10,2,5] 从小到大排序 不许使用sort
输出 [2,3,4,5,5,7,9,10]
"""
from typing import List


def SortList(nums: List) -> List:
	m = nums[0]
	n = []
	for i in (1, len(nums)):
		if nums[i] < m:
			m = nums[i]
		nums.remove(m)
