class Solution(object):
    def isPalindrome(self, x):
        xs = str(x)
        if (xs == xs[::-1]):
            return True
        else:
            return False
        