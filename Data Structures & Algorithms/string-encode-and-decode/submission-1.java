class Solution {

    public  String encode(List<String> strs) {
        StringBuilder es = new StringBuilder();
        for(String s: strs)
        {
           es.append(s.length()+"#"+s);
        }

        return es.toString();

    }

    public  List<String> decode(String str) {
              List<String> resultList = new ArrayList<>();

        int i=0;
        while(i<str.length())
        {
            int j =i;
            StringBuilder count = new StringBuilder();
            while(str.charAt(j)!='#')
            {
                count = count.append(str.charAt(i));
                j++;
            }
            int length= Integer.parseInt(str.substring(i,j));
            i=j+1+length;
            resultList.add(str.substring(j+1,i));

        }
        return resultList;
    }
}
