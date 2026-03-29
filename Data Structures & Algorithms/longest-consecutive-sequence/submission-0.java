class Solution {
    public int longestConsecutive(int[] nums) {
        int maxLength =0;
        Set<Integer> lookUp = new HashSet<>();
        for(int n:nums)
        {
            lookUp.add(n);
        }

        for(Integer value:lookUp)
        {
            //check ig beginning of sequence
            if(!lookUp.contains(value-1))
            {
                int length =1;int start =value;
                while(lookUp.contains(start+1))
                {
                    length++;start++;

                }
                maxLength = Math.max(length,maxLength);
            }
        }
        return maxLength;
    }
}
