class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Pointer for placement of elements not equal to val

        # Iterate over each element in the list
        for i in range(len(nums)):
            if nums[i] != val:  # If the element is not equal to val
                nums[k] = nums[i]  # Move it to the k-th position
                k += 1  # Increment k
        
        return k
