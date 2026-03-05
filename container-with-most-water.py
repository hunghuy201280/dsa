from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            result = max(area, result)
            if heights[l] <= heights[r]:
                l += 1
                continue
            else:
                r -= 1
                continue
        return result


if __name__ == "__main__":
    s = Solution()
    res = s.maxArea([1, 7, 2, 5, 4, 7, 3, 6])
    print(res)
    res = s.maxArea([2, 2, 2])
    print(res)
