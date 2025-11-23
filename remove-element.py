from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1

        return k


if __name__ == "__main__":
    s = Solution()
    res = s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    # res = s.removeElement([3,3], 3)
    print(res)
