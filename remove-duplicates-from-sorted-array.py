from typing import List


class Solution:
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        actualLen = len(nums)
        for i in range(actualLen):
            if i + 1 == actualLen:
                return actualLen
            while i + 1 < actualLen and nums[i] == nums[i + 1] :
                for j in range(i, actualLen - 1):
                    nums[j] = nums[j + 1]
                actualLen -= 1

        return actualLen

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        nextUniqueIndex = 1
        currentVal=nums[0]
        removedCount = 0
        for i in range(1,len(nums)):
            if nums[i]!=currentVal:
                nums[nextUniqueIndex]=nums[i]
                nextUniqueIndex+=1
                currentVal=nums[i]
                continue
            removedCount+=1



        return len(nums)-removedCount

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        l=1
        r=1
        while r<len(nums):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1
            r+=1
        return l



if __name__ == "__main__":
    s = Solution()
    # res = s.removeDuplicates([1,1])
    res = s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    # res = s.removeDuplicates([1,2,2])
    print(res)

