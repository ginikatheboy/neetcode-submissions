class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = (m*n) - 1

        while l <= r:
            mid_ind = (l+r) // 2
            i = mid_ind // n
            j = mid_ind % n
            mid_num = matrix[i][j]

            if mid_num == target:
                return True
            elif mid_num < target:
                l = mid_ind + 1
            else:
                r = mid_ind - 1

        return False
        