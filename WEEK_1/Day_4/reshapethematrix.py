class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat) #rows
        n = len(mat[0]) #colums

        if m * n != r * c:
             return mat
        ans = [[0] * c for _ in range(r)]

        for x in range(m * n):
            ans[x//c][x%c] = mat[x//n][x%n]
        return ans