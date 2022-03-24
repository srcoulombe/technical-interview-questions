class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:       
        # setup
        ## first we create a len(text1) x len(text2) array
        ## where alignment_array[i][j] holds the longest common
        ## subsequence between text1[:i] and text2[:j]
        alignment_array = []
        for row in range(len(text1)):
            alignment_array.append([0]*len(text2))
        
        ## need to start by populating all of the first row,
        ## and all of the first column
        alignment_array[0][0] = int(text1[0] == text2[0])
        for r_i in range(1, len(text1)):
            alignment_array[r_i][0] = max(
                alignment_array[r_i-1][0],
                int(text1[r_i] == text2[0])
            )
        for c_i in range(1, len(text2)):
            alignment_array[0][c_i] = max(
                alignment_array[0][c_i-1],
                int(text1[0] == text2[c_i])
            )
        
        # calculation
        ## at each step, you calculate the longest common subsequence
        ## between text1[:i] and text2[:j]. 
        for r_i in range(1,len(text1)):
            for c_i in range(1,len(text2)):
                alignment_array[r_i][c_i] = max(
                    alignment_array[r_i-1][c_i-1] + int(text1[r_i] == text2[c_i]),
                    alignment_array[r_i][c_i-1],
                    alignment_array[r_i-1][c_i]
                )
        longest = 0
        for r_i in range(len(text1)):
            for c_i in range(len(text2)):
                longest = max(longest, alignment_array[r_i][c_i])
        return longest
