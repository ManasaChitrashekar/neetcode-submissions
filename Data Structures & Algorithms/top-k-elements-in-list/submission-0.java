class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //build look up ;
        Map<Integer,Integer> lookUp = new HashMap<>();
        for(int i : nums)
        {
            lookUp.put(i,lookUp.getOrDefault(i,0)+1);
        }

        //build the min heap and poll min values from heap when size >k
        //once all values in map are processed heap will have k elements 

        Iterator<Map.Entry<Integer,Integer>> lookUpIt = lookUp.entrySet().iterator();

        //create a min heap 
        PriorityQueue<Map.Entry<Integer,Integer>> minHeap =
                new PriorityQueue<>((n1,n2)->(n1.getValue()-n2.getValue()));
        while(lookUpIt.hasNext())
        {
            minHeap.add(lookUpIt.next());
            if(minHeap.size()>k)
                minHeap.poll();
        }

        int[] resArr = new int[k];
        int index=0;

        while(!minHeap.isEmpty())
        {
            resArr[index] = minHeap.poll().getKey();
            index++;
        }

        return resArr;
    }
}
