class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Step 1: Handle edge case for an empty matrix
        if not matrix:
            return
        
        # Step 2: Get the dimensions of the matrix
        rows, cols = len(matrix), len(matrix[0])
        
        # Step 3: Create a deep copy of the original matrix
        copy_matrix = [row[:] for row in matrix]
        
        # Step 4: Traverse the original matrix to find zeros
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    # Step 5: Mark the entire row with zeros in the copied matrix
                    for k in range(cols):
                        copy_matrix[row][k] = 0
                    # Step 6: Mark the entire column with zeros in the copied matrix
                    for k in range(rows):
                        copy_matrix[k][col] = 0
        
        # Step 7: Copy the updated values back to the original matrix
        for row in range(rows):
            for col in range(cols):
                matrix[row][col] = copy_matrix[row][col]

        # Why deep copy?
        # Using a deep copy prevents discrepancies that could occur
        # if we modified the original matrix during iteration.