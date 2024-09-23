class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1  # Pointer for placement of elements not equal to val

        # Iterate over each element in the list
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:  # If the element is not equal to val
                nums[k] = nums[i]  # Move it to the k-th position
                k += 1  # Increment k
        
        return k