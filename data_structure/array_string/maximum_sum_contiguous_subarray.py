
class Solution:
    def maximumSumContiguousSubarray(self, nums):
        maxSum = nums[0]
        currentSum = 0

        for i in nums:

            if currentSum < 0:
                currentSum = 0
            currentSum += i

            maxSum = max(maxSum,currentSum)
            
        return maxSum






nums = [1,-1,2,-2,3]
print(Solution().maximumSumContiguousSubarray(nums))   
