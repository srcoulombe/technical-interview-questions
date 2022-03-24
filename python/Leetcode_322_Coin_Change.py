import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0: 
            if amount > 0:
                return -1
            else:
                return 0
        coins = sorted(coins)
        coins_needed_to_get_to_i = [0]+[sys.maxsize]*(amount)
        for i in range(amount+1):
            num_coins_needed_to_get_to_here = coins_needed_to_get_to_i[i]
            for c in coins:
                if c > i: 
                    break
                else:
                    num_coins_needed_to_get_to_here = min(
                        num_coins_needed_to_get_to_here,
                        coins_needed_to_get_to_i[i-c]+1
                    )
            
            coins_needed_to_get_to_i[i] = num_coins_needed_to_get_to_here
        answer = coins_needed_to_get_to_i[~0]
        if answer == sys.maxsize:
            answer = -1
        return answer
