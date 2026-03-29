class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        int max = piles[piles.length-1];
        int k = max;
        int low = 1,high = max;
        while(low<=high)
        {
            int mid = (low+high)/2;
            int res =0;
            for(int i =0;i<piles.length;i++)
            {
                 res+=  Math.ceil((double)piles[i]/mid);
            }
            if(res<=h)
            {
                k = mid;
                high = mid -1;
            }
            else
            {
                low = mid+1;
            }

        }
        return k;
    }
}
