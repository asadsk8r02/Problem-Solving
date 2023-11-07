# class Solution:
#     def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
#         for i in range(1,len(dist)):
#             for j in range(i, len(dist)):
#                 dist[j] = dist[j]-speed[j]
#                 if dist[j]<0:
#                     dist[j]=0

#             if dist[i] == 0:
#                 return i

#         return len(dist)

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time_to_reach = [dist[i] / speed[i] for i in range(n)]
        time_to_reach.sort()

        for i in range(n):
            if time_to_reach[i] <= i:
                return i

        return n

            