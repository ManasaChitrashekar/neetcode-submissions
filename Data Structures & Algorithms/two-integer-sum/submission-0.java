class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> lu= new HashMap<Integer,Integer>();
        for(int i =0;i<nums.length;i++)
        {
            int value = target-nums[i];
            if(lu.get(value)!=null)
            {
                int comp = lu.get(value);
                if(comp>i)
                    return new int[]{i,comp};
                else
                    return new int[]{comp,i};  
            }
            else
            {
                lu.put(nums[i],i);
            }
        }
        return new int[]{0,0};
    }
}
