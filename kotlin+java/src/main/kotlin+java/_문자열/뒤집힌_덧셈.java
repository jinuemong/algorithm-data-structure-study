package _문자열;

import java.util.Scanner;

public class 뒤집힌_덧셈 {
    public static int reverse(int num) {
        int reversed = 0;
        while (num > 0) {
            reversed = reversed * 10 + num % 10;
            num /= 10;
        }
        return reversed;
    }

    public static int reverse2(int num) {
        StringBuilder sb = new StringBuilder(String.valueOf(num));
        return Integer.parseInt(sb.reverse().toString());
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt();
        int Y = sc.nextInt();

        int reversedSum = reverse(reverse(X) + reverse(Y));

        System.out.println(reversedSum);

        int reversedSum2 = reverse2(reverse2(X) + reverse2(Y));

        // 결과 출력
        System.out.println(reversedSum2);

        sc.close();
    }

}
