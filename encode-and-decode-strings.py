from typing import List


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"
        return result

    # write your code here

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s) -> List[str]:
        i = 0
        num = ""
        res = []
        while i < len(s):
            if s[i] != "#":
                num += s[i]
            else:
                i += 1
                strLen = int(num)
                str = s[i: i + strLen]
                i += strLen - 1
                res.append(str)
                num = ""
            i += 1

        return res

    # write your code here


if __name__ == "__main__":
    s = Solution()
    res = s.encode(["lint", "code", "love", "you"])
    print(res)
    res1 = s.decode(res)
    print(res1)
