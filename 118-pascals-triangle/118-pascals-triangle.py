class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        triangles = [[1]]
        for num in range(1, numRows):
            row = []
            for i in range(num+1):
                if i == 0:
                    row.append(triangles[num-1][0])
                elif i == num:
                    row.append(triangles[num-1][-1])
                else:
                    row.append(triangles[num-1][i-1]+triangles[num-1][i])
            triangles.append(row)
        return triangles

a = Solution()
print(a.generate(3))