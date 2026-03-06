from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        curSum=0
        for n in nums:
            curSum=max(curSum,0)
            curSum+=n
            maxSum=max(curSum,maxSum)
        return maxSum
    def maxSubArray2Pointer(self, nums: List[int]) -> List[int]:
        maxSum=nums[0]
        curSum=0
        l=0
        maxL,maxR=0,0
        for r in range(len(nums)):
            n=nums[r]
            if curSum<0:
                curSum=0
                l=r
            curSum+=n
            if curSum>maxSum:
                curSum=maxSum
                maxL=l
                maxR=r
        return [maxL,maxR,maxSum]


if __name__ == "__main__":
    s = Solution()
    res = s.maxSubArray([2, -3, 4, -2, 2, 1, -1, 4])
    print(res)

    res = s.maxSubArray([-1]
                        )
    print(res)
    res = s.maxSubArray2Pointer([2, -3, 4, -2, 2, 1, -1, 4])
    print(res)

    res = s.maxSubArray2Pointer([-1]
                        )
    print(res)
