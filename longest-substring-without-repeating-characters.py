from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0

        strSet=set()
        l=0
        maxLength=1

        for r in range(len(s)):
            c=s[r]

            while c in strSet:
                strSet.remove(s[l])
                l+=1

            maxLength=max(maxLength,r-l+1)
            strSet.add(c)

        if len(strSet)==len(s):
            return len(s)

        return  maxLength



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
    res = s.lengthOfLongestSubstring("aab")
    print(res)
    res = s.lengthOfLongestSubstring("abcabcbb")
    print(res)

    res = s.lengthOfLongestSubstring("bbbbb")
    print(res)
    res = s.lengthOfLongestSubstring("pwwkew")
    print(res)
    res = s.lengthOfLongestSubstring("au")
    print(res)
    res = s.lengthOfLongestSubstring("dvdf")
    print(res)
    res = s.lengthOfLongestSubstring("pwwkew")
    print(res)
