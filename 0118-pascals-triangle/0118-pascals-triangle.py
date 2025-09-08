class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        triangle = [[1], [1, 1]]

        for i in range(2, numRows):
            prev_row = triangle[i-1]
            row = [1]

            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])

            row.append(1)
            triangle.append(row)

        return triangle
