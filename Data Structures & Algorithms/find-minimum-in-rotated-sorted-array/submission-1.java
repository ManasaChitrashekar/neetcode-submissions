class Solution {
    public int findMin(int[] nums) {
        int min =nums[0];
        int low = 0,high =nums.length-1;
        while(low<high)
        {
            if(nums[low]>nums[low+1] )
                return nums[low+1];
            else if ( nums[high]<nums[high-1])
                return nums[high];
            else
            {
                low++;
                    high--;
            }

        }
        return min;
    }
}
