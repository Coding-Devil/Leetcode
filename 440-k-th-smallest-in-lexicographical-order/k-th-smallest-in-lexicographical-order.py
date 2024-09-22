class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def calculate_steps(n, current, next):
            steps = 0
            while current <= n:
                steps += min(n + 1, next) - current
                current *= 10
                next *= 10
            return steps
        
        current = 1
        k -= 1  # Start from the first number
        
        while k > 0:
            steps = calculate_steps(n, current, current + 1)
            if k >= steps:
                # Move to the next number
                current += 1
                k -= steps
            else:
                # Go deeper (to the next level, by multiplying by 10)
                current *= 10
                k -= 1
        
        return current
