#You are climbing a staircase. It takes n steps to reach the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# 
#
#Example 1:
#
#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#
#Example 2:
#
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
#
# 
#
#Constraints:
#
#    1 <= n <= 45
#
#
class Solution:
    def climbStairs(self, n: int) -> int:
        # the trick is to realize that 
        # the first 'step' you take either
        # brings you to the n-1 case (if you 
        # take a normal step) or to the n-2 case
        # (if you take a double step). 
        
        # some easy cases
        if n <= 0: return 0
        elif n == 1: return 1
        elif n == 2: return 2
        else:
            x = [1,2]
            to_change = 0
            for m in range(3,n+1):
                x[int(to_change)] = sum(x)
                to_change = (to_change + 1) % 2
            return max(x)
