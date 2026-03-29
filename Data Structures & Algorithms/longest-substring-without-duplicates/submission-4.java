class Solution {
    public int lengthOfLongestSubstring(String s) {
         if(s.length()==0) return 0;
        if(s.length()==1) return 1;
        int res=0,i=0;
        Set<Character> uniqSet = new HashSet<>();
        for(int j=0;j<s.length();j++)
        {
            while (uniqSet.contains(s.charAt(j))) {

                uniqSet.remove(s.charAt(i));
                i++;
            }
            uniqSet.add(s.charAt(j));
            res = Math.max(res, j - i + 1);
        }
        return res;
    }
}
