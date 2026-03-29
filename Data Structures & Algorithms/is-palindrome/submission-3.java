class Solution {
    public boolean isPalindrome(String s) {
       s=s.toLowerCase(Locale.ROOT);
       int left =0,right=s.length()-1;
       while(left<=right)
       {
           while (left<s.length() && !Character.isLetterOrDigit(s.charAt(left)))
           {
               left++;
           }
           while   (right>=0 && !Character.isLetterOrDigit(s.charAt(right)))
           {
               right--;
           }
           if(left<s.length() && right>=0 && s.charAt(right)!=s.charAt(left))
           {
               return false;
           }

           left++;right--;
       }
        return true; 
    }
}
