class MinStack {

     Stack<Integer> st ;
    Stack<Integer> mst;
    
    public MinStack() {
        st = new Stack<Integer>();
        mst = new Stack<Integer>();
    }

    public void push(int val) {
         st.push(val);
         val = Math.min(val, mst.isEmpty() ? val : mst.peek());
         mst.push(val);
       
    }

    public void pop() {
        st.pop();
        mst.pop();
    }

    public int top() {
        return st.peek();
    }

    public int getMin() {
        return mst.peek();
    }
}
