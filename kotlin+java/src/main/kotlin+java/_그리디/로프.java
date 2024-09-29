package _그리디;

import java.util.*;

public class 로프 {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int n  = sc.nextInt();
        int [] lop = new int[n];
        for (int i = 0; i<n; i++){
            lop[i] = sc.nextInt();
        }

        Arrays.sort(lop);
        int result = 0;
        for (int i = 0; i<n; i++){
            result = Math.max(result,lop[i] * (n-i));
        }
        System.out.println(result);
    }
}
