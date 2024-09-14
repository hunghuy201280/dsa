from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nLen = len(nums)
        res = [1 for x in range(nLen)]
        cur = 1
        # zeroIndex = -1
        for i in range(nLen):
            # if zeroIndex != -1 and nums[i] == 0:
            #     return [0 for x in range(nLen)]
            # elif zeroIndex == -1 and nums[i] == 0:
            #     zeroIndex = i
            res[i] *= cur
            cur *= nums[i]

        cur = 1
        for i in range(nLen - 1, -1, -1):
            res[i] *= cur
            cur *= nums[i]
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.productExceptSelf([1, 2, 3, 4])
    print(res)
    res = s.productExceptSelf([-1, 1, 0, -3, 3])
    print(res)
