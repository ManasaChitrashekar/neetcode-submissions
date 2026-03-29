class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> opSt = new Stack<Integer>();
        for(String s:tokens)
        {
            switch(s)
            {
                case "+" :
                {
                    Integer one = opSt.pop();
                    Integer two = opSt.pop();
                    opSt.push(one + two );
                    break;
                }
                case "-" :
                {
                    Integer one = opSt.pop();
                    Integer two = opSt.pop();
                    opSt.push(two-one );
                    break;
                }
                case "*" :
                {
                    Integer one = opSt.pop();
                    Integer two = opSt.pop();
                    opSt.push(one * two );
                    break;
                }
                case "/" :
                {
                    Integer one = opSt.pop();
                    Integer two = opSt.pop();
                    if(one==0)
                        opSt.push( 0);
                    else    
                        opSt.push( two / one);
                    break;
                }
                default:
                    opSt.push(Integer.parseInt(s));
            }
        }
        return opSt.pop();
    }
}
