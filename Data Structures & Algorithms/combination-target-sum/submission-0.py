class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]
        def dfs(index,subset,sum):
        
            if(sum == target):
                res.append(subset.copy())
                return 
            if (index>=len(nums) or sum>target):
                return    

            subset.append(nums[index])
            dfs(index,subset,sum+ nums[index])
            subset.pop()
            dfs(index+1,subset,sum)

        dfs(0,[],0)   
        return res          
