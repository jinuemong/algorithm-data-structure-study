package _그리디;

import java.util.*;

public class ATM {
    public static void main(String [] args){
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        scanner.nextLine();

        String[] input = scanner.nextLine().split(" ");
        int [] numbers = new int[n];
        for (int i = 0; i < n; i++ ){
            numbers[i] = Integer.parseInt(input[i]);
        }
        numbers = Arrays.stream(numbers).sorted().toArray();
        for (int i = 1; i < n; i++){
            numbers[i] += numbers[i-1];
        }
        int result = 0;
        for(int i = 0; i < n; i++){
            result += numbers[i];
        }
        System.out.println(result);
    }
}
