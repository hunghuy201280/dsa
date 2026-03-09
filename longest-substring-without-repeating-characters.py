from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s):

        strSet=set()
        l=0
        maxLength=0
        for r in range(len(s)):
            c=s[r]
            if c in strSet:
                maxLength=max(maxLength,r-l)
                l=r

            strSet.add(c)
        return maxLength



#Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


if __name__ == "__main__":
    s = Solution()
    res = s.lengthOfLongestSubstring("abcabcbb")
    print(res)

    res = s.lengthOfLongestSubstring("bbbbb")
    print(res)
    res = s.lengthOfLongestSubstring("pwwkew")
    print(res)
