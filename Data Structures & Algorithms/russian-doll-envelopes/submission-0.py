class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
            sort envelopes based on width , its given that we can use it
         only when both width and height is diffrent , here we are trying to put small envelope to
          brigger on and so on , we shouldnt accidnetly count envelopes with same with so negate it 
          by sorting height in descending 
        """

        envelopes.sort(key = lambda x : (x[0],-x[1]))
        #convert to single sequence 
        heights = []
        for w,h in envelopes:
            heights.append(h)

       
        n = len(heights) 
        dp = [1]*(n+1)
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if heights[i]<heights[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)