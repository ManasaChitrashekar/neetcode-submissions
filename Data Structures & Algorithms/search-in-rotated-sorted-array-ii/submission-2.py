class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if (target==nums[mid]):
                return True
            # Handle the case where nums[l] == nums[mid] == nums[r]
            if nums[l] == nums[mid]:
                l += 1
            #check if nubers are in order consdering mid always belongs to left if loeft is sorted 
            elif nums[l]<nums[mid]:
                 #check if target is in left range 
                 if nums[l]<=target<nums[mid]:
                    r= mid-1
                 else:
                    l=mid+1
            else:
                #check if target is in right range 
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return False