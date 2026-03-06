from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum=nums[0]
        totalSum=0
        curMaxSum = 0
        curMinSum = 0
        # duplicate the array
        for i in range(len(nums)):
            n=nums[i]
            totalSum+=n
            if curMaxSum < 0:
                curMaxSum = 0
            curMaxSum += n
            if curMaxSum > maxSum:
                maxSum = curMaxSum

            if curMinSum>0:
                curMinSum=0
            curMinSum+=n
            if curMinSum<minSum:
                minSum=curMinSum

        if totalSum==minSum:
            return maxSum
        return max(maxSum,totalSum-minSum)


if __name__ == "__main__":
    s = Solution()
    res = s.maxSubarraySumCircular([1, -2, 3, -2])
    print(res)

    res = s.maxSubarraySumCircular([5, -3, 5])
    print(res)
    res = s.maxSubarraySumCircular([-3,-2,-3])
    print(res)
