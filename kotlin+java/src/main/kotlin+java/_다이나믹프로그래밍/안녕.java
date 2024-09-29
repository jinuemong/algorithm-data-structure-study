package _다이나믹프로그래밍;

import java.util.Scanner;

public class 안녕 {
    public static void main (String [] args){
        Scanner sc = new Scanner(System.in);
        int n  = sc.nextInt();
        int k = 99;

        int [][] dp = new int[n+1][k+1];
        int [] L = new int[n+1];
        int [] J = new int[n+1];
        for (int i = 1; i<=n; i++){
            L[i] = sc.nextInt();
        }
        for (int i = 1; i<=n; i++){
            J[i] = sc.nextInt();
        }

        for (int i = 1; i<=n; i++){
            for (int j = 0; j<=k; j++){
                if (L[i]<=j){
                    dp[i][j] = Math.max(dp[i-1][j-L[i]]+J[i],dp[i-1][j]);
                } else{
                    dp[i][j] = dp[i-1][j];
                }
            }
        }

        System.out.println(dp[n][k]);
    }
}
