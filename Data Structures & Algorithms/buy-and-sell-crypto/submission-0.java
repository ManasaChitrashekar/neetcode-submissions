class Solution {
    public int maxProfit(int[] prices) {
         int profit =0;
        int l =0;
        for(int r =1;r<prices.length;r++)//r always advances
        {
            if(prices[l]<prices[r])
            {
                profit = Math.max(prices[r]-prices[l],profit);
            }
            else
            {
                //left doesnt give profit so move it to where right is as we covered all proces between these two points
                l=r;
            }
        }
        return profit;
    }
}
