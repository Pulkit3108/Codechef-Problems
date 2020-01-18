import java.util.*;
import java.lang.*;
import java.io.*;
public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner scan = new Scanner(System.in);
	    long T = scan.nextLong();
	    while(T-->0){
	        int N = scan.nextInt();
	        long[] S = new long[N];
	        int i;
	        long c,d;
	        for(i=0;i<N;i++){
	            S[i] = scan.nextLong();
	        }
	        Arrays.sort(S);
	        d=S[1]-S[0];
	        for(i=0;i<N-1;i++){
	            if((S[i+1]-S[i])<d && (S[i+1]-S[i])>=0){
	                d = S[i+1] - S[i];
	            }
	        }
	        System.out.println(d);
	   }
    }
}
