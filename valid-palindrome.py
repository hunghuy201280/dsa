from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        ordA=ord('a')
        ordZ=ord('z')
        ord0=ord('0')
        ord9=ord('9')
        while l<r :
            ordR=ord(s[r].lower())
            ordL=ord(s[l].lower())
            if (ordL>ordZ or ordL<ordA) and (ordL>ord9 or ordL<ord0) :
                l+=1
                continue
            if (ordR>ordZ or ordR<ordA) and (ordR>ord9 or ordR<ord0) :

                r-=1
                continue
            if ordL!=ordR:
                return False
            l+=1
            r-=1
        return True


if __name__ == "__main__":
    s = Solution()
    res = s.isPalindrome("Was it a car or a cat I saw?")
    print(res)
    res = s.isPalindrome("tab a cat")
    print(res)

