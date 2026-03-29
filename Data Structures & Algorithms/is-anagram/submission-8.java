class Solution {
    public boolean isAnagram(String s, String t) {
       if(s.length()!=t.length()) return false;
        Map<Character,Integer> lookUp = new HashMap<>();
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();


        for(int i = 0; i<s.length(); i++){
            if( lookUp.get(sArr[i])==null)
            {
                lookUp.put(sArr[i],1);
            }
            else
                lookUp.put(sArr[i],lookUp.get(sArr[i])+1);
        }

        for(int i=0;i<tArr.length;i++)
        {
            if(lookUp.get(tArr[i])!=null)
            {
                lookUp.put(tArr[i],lookUp.get(tArr[i])-1);
                if(lookUp.get(tArr[i])==0)
                    lookUp.remove(tArr[i]);
            }
            else
                return false;
        }


        return lookUp.isEmpty();
}
}
