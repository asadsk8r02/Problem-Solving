class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # j=0
        # winner = arr[0]
        # while j<k:
        #     temp_win = max(arr[0],arr[1])
        #     if winner == temp_win:
        #         arr.append(arr.pop(min(arr[0],arr[1])))
        #         j+=1
        #     else:
        #         winner = temp_win
        #         arr.append(arr.pop(min(arr[0],arr[1])))
        #         j=1
            

        # return winner

        winner = arr[0]
        consecutive_wins = 0
        
        for i in range(1, len(arr)):
            if arr[i] > winner:
                winner = arr[i]
                consecutive_wins = 1
            else:
                consecutive_wins += 1
            
            if consecutive_wins == k:
                return winner
        
        return winner