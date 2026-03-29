class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        i = 0
        op = []
        res = []
        

        def subset(index,nums,op,res):
            if(index>=len(nums)):
                res.append(op.copy())
                return    
            op.append(nums[index])
            subset(index+1,nums,op,res)
            op.pop()
            subset(index+1,nums,op,res)

        subset(i,nums,op,res)
        return res    