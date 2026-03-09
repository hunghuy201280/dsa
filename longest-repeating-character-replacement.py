from collections import defaultdict
from typing import List


class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l=0
        maxLength=1
        freq=defaultdict(int)
        for r in range(len(s)):
            freq[s[r]]+=1
            maxFreq=max(freq.values())

            curLen=r-l+1
            if curLen-maxFreq>k:
                freq[s[l]]-=1
                l+=1
                curLen=r-l+1
            maxLength=max(curLen,maxLength)




        return maxLength



#
# Example 1:
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

# aababba
# l   r -> 4, 1
#  l  r
#   l r -> 3, 1
#   l   r
#    l


if __name__ == "__main__":
    s = Solution()
    res = s.characterReplacement("ABAB",2)
    print(res)

    res = s.characterReplacement("AABABBA",1)
    print(res)
