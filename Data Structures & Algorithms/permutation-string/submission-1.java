class Solution {
    public boolean checkInclusion(String s1, String s2) {
        Map<Character,Integer> s1Count = new HashMap<>();
        Map<Character,Integer> s2Count = new HashMap<>();
        int i=0;
        for(char c: s1.toCharArray())
        {
            s1Count.put(c,s1Count.getOrDefault(c,0)+1);
        }
        for(int j=0;j<s2.length();j++)
        {

            s2Count.put(s2.charAt(j),s2Count.getOrDefault(s2.charAt(j),0)+1);
            if(j-i+1==s1.length())
            {
                if(s1Count.equals(s2Count))
                    return true;
            }
            if(j-i+1>s1.length())
            {

                if(s2Count.get(s2.charAt(i))!=null)
                {
                    s2Count.put(s2.charAt(i),s2Count.get(s2.charAt(i))-1);
                    if(s2Count.get(s2.charAt(i))==0)
                        s2Count.remove(s2.charAt(i));
                    i++;
                }
                if(s1Count.equals(s2Count))
                    return true;
            }
        }
        return false;
    }
}
