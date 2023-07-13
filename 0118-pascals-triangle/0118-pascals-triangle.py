class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # l = [[1]]
        # if numRows == 1:
        #     return [[1]]
        
        # for i in range(1, numRows):
        #     first = l[i - 1][0]
        #     last = l[i - 1][-1]

        #     l_temp = []
        #     for k in range(len(l[i - 1]) - 1):
        #         l_temp.append(l[i - 1][k] + l[i - 1][k + 1])

        #     l_temp.insert(0, first)
        #     l_temp.append(last)

        #     l.append(l_temp)
        
        # return l
        triangle = []
    
        for row in range(numRows):
            # Create a new row with 1s at the beginning and end
            new_row = [1] * (row + 1)
            
            # Fill the middle elements of the row
            for i in range(1, row):
                new_row[i] = triangle[row - 1][i - 1] + triangle[row - 1][i]
            
            triangle.append(new_row)
        
        return triangle

