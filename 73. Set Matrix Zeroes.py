# https://leetcode.com/problems/set-matrix-zeroes/description/
# time complexity : O(n*m)
# space comlexity : O(n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        zero = []

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero.append([i,j])

        for c in zero:
            for i in range(row):
                matrix[i][c[1]] = 0

            for i in range(col):
                matrix[c[0]][i] = 0

        return matrix