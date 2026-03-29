class Solution {
public static List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> anagramGroupList = new ArrayList<>();
        List<String> anagramList = new ArrayList<>();

        for(int i=0;i<strs.length;i++)
        {
            char[] valueToSort = (strs[i].toCharArray());
            Arrays.sort(valueToSort);
            String sortedString = new String(valueToSort);
            if(!anagramList.contains(sortedString))
            {
                List<String> subList = new ArrayList<>();
                subList.add(strs[i]);
                for(int j = 0;j<strs.length ;j++)
                {
                    if(j!=i && isAnagram(strs[i],strs[j]))
                    {
                        subList.add(strs[j]);
                    }
                }
                anagramGroupList.add(subList);
                anagramList.add(sortedString);
            }

        }
        return anagramGroupList;
    }

    public static boolean isAnagram(String s, String t) {
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
