
/* 
  Head and Tails Program
*/


import java.util.*;

public class toss
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i, c, h = 0, t = 0;
        double d;
        for(i = 1; i<=20; i++)
        {
            d = Math.random()*2;
            c = (int)d;
            if(c == 1)
            {
                h = h + 1;
            }
            else
            {
                t = t+1;
            }
       
     System.out.println("No. of times Heads obtained = "+h);
     System.out.println("No. of times Tails obtained = "+t);
        }
    }
}
