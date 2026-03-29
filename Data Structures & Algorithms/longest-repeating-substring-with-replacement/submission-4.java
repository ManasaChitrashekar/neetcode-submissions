class Solution {
    public int characterReplacement(String s, int k) {
         int start=0;
        Map<Character,Integer> lookupMap = new HashMap<Character,Integer>();
        int res =0;
        int maxF= 0;
        char[] sarr =s.toCharArray();
        for(int end =0;end<sarr.length;end++)
        {
            lookupMap.put(sarr[end],lookupMap.getOrDefault(sarr[end],0)+1);
            maxF = getMaxFromMap(lookupMap);
              if(end-start+1-maxF<=k)
            {
                res = Math.max(res,end-start+1);
            }
            if(end-start+1-maxF>k)
            {
                if(lookupMap.get(sarr[start])!=null){
                    lookupMap.put(sarr[start],lookupMap.get(sarr[start])-1);
                    start++;
                }
            
            }
        }
        return res;
    }

    private static int getMaxFromMap(Map<Character, Integer> map) {
        Character key = Collections.max(map.entrySet(), Map.Entry.comparingByValue()).getKey();
        return map.get(key);
    }
}
