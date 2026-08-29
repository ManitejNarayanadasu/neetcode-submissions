class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        total = rows * columns

        l = 0 
        r = total - 1 

        while l<=r:
            m = (l+r)//2
            i = m // columns
            j = m % columns

            mid_num = matrix[i][j]

            if target < mid_num:
                r = m - 1
            elif target > mid_num:
                l = m + 1
            else:
                return True
        return False
        