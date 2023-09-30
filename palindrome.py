# given a string "s", determine if it is a palindrome, considering only alphabetic 
# characters and ignoring cases.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            while l < r and not alphaNum(s[r]):
                r -= 1


            if s[1].lower() != s[r].lower():
                return False

            l, r = l + 1, r -1
        return True

    def alphaNum(self, c):
        return (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('0') and ord(c) <= ord('9'))

