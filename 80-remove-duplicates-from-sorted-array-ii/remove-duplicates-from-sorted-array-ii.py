class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        k = 2  # Pointer for placement of unique elements (start from 1 since first element is always unique)
        
        # Iterate over the list starting from the second element
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:  # If current element is not the same as the previous one
                nums[k] = nums[i]  # Place it in the k-th position
                k += 1  # Increment k
        
        return k