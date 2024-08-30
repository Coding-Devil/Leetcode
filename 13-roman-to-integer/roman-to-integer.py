class Solution(object):
    def romanToInt(self, s):
        dict = {
            'I': 1, 
            'V': 5, 
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        val = 0
        for i in range(len(s)):
            if s[i] in dict:
                if i + 1 < len(s) and dict[s[i]] < dict[s[i + 1]]:
                    val -= dict[s[i]]
                else:
                    val += dict[s[i]]
        return val  