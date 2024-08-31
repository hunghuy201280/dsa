from typing import List

from black.trans import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for stri in strs:
            charCount = [0] * 26
            for c in stri:
                charCount[ord(c) - ord("a")] += 1
            ht[tuple(charCount)].append(stri)
        return [x for x in (ht.values())]


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for stri in strs:
            temp = [x for x in stri]
            temp.sort()
            ht["".join(temp)].append(stri)
        return [x for x in (ht.values())]


if __name__ == "__main__":
    s = Solution()
    res = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)
    s = Solution2()
    res = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)
