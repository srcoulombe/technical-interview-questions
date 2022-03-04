#Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
#A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
# 
#
#Example 1:
#
#Input: nums = [10,9,2,5,3,7,101,18]
#Output: 4
#Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
#Example 2:
#
#Input: nums = [0,1,0,3,2,3]
#Output: 4
#
#Example 3:
#
#Input: nums = [7,7,7,7,7,7,7]
#Output: 1
#
# 
#
#Constraints:
#
#    1 <= nums.length <= 2500
#    -104 <= nums[i] <= 104
#
#Link: https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # recall that dynamic programming is about breaking
        # the problem into smaller problems s.t. the overall
        # solution can be derived from the sub-solutions.
        # with that being said, tackling the problem from 
        # left->right doesn't actually create useful sub-problems
        # but tackling it from right->left does!
        
        LIS_at_i = [1] * len(nums)
        # -1 because we already know that the LIS 
        # starting at the last number is of length 1
        for i in reversed(list(range(0, len(nums)))):
            length_of_LIS_starting_here = 1 + max([
                LIS_at_i[ii] if nums[i] < nums[ii] else 0
                for ii in range(i, len(nums))
            ])
            LIS_at_i[i] = length_of_LIS_starting_here
        return max(LIS_at_i)
