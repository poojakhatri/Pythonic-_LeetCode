class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        palindrome = ""
        for char in s:
            if char.isalnum():
                palindrome += char.lower()
        return palindrome == palindrome [::-1]
        