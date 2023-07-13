# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         t = []
#         for row in range(rowIndex+1):
#             temp = [1]*(row+1)
#             for i in range(1, row):
#                 temp[i] = t[row-1][i-1] + t[row-1][i]

#             t.append(temp)

#         return t[rowIndex]
        
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ar = [1 for i in range(rowIndex + 1)]
        
        for i in range(1, rowIndex//2+1):
            ar[i] = ar[i-1] * (rowIndex - i + 1)//i
            ar[rowIndex - i] = ar[i]
      
        return ar       