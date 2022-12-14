"""
152. 乘积最大子数组
给你一个整数数组 nums，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。


示例 1:

输入: [2,3,-2,4]
输出: 6
解释:子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释:结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def maxProduct(nums):
	"""
	暴力
	:param nums:
	:return:
	"""
	if len(nums) == 1:
		return nums[0]
	maxres = nums[0]
	for i in range(0, len(nums)):
		curmax = 1
		for j in range(i, len(nums)):
			curmax = curmax * nums[j]
			maxres = max(curmax, maxres)
	return maxres


def maxProduct2(nums):
	"""
	DP
	:param nums:
	:return:
	"""
	if len(nums) == 1:
		return nums[0]
	maxres = curmin = curmax = nums[0]
	for i in range(1, len(nums)):
		if nums[i] < 0:
			curmax, curmin = curmin, curmax
		curmax = max(curmax*nums[i], nums[i])
		curmin = min(curmin*nums[i], nums[i])
		maxres = max(maxres, curmax)
	return maxres


print(maxProduct([2, 3, -2, 4]))
