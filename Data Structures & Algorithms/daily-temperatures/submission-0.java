class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
         List<Integer> res = new ArrayList<>();
        Stack<Pair> st = new Stack<>();
        for(int i = temperatures.length-1;i>=0;i--)
        {
            if(st.isEmpty())
            {
                res.add(0,0);
            }
            else if(!st.isEmpty() && st.peek().temp>temperatures[i])
            {
                res.add(0,st.peek().index-i);
            }
            if(!st.isEmpty() && temperatures[i] >= st.peek().temp)
            {
                while(!st.isEmpty() && temperatures[i] >= st.peek().temp)
                {
                    st.pop();
                }
                if(st.isEmpty())
                {
                    res.add(0,0);
                }
                else
                {
                    res.add(0,st.peek().index-i);
                }
            }


            st.push(new Pair(temperatures[i],i));

        }
        return res.stream().mapToInt(i->i).toArray();
    }
    private  class Pair {
        int temp;
        int index;

        public Pair(int temperature, int i) {
            temp=  temperature;
            index = i;
        }
    }
}
