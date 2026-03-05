from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=set()
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum==0:
                    result.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                    continue
                elif sum >0:
                    r-=1
                    continue
                else:
                    l+=1
                    continue

        resList=list(result)
        return [[a,b,c] for (a,b,c) in resList]




if __name__ == "__main__":
    s = Solution()
    res = s.threeSum( [-1,0,1,2,-1,-4])
    print(res)

