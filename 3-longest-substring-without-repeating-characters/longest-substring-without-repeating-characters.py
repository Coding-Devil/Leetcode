class Solution(object):
    def lengthOfLongestSubstring(self,s):
        current_chars = set()
        max_len = 0
        start = 0
    
        for end in range(len(s)):
            while s[end] in current_chars:
                current_chars.remove(s[start])
                start += 1
            current_chars.add(s[end])
            max_len = max(max_len, end - start + 1)
    
        return max_len