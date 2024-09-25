package _그리디;

import java.util.Scanner;
import java.util.Stack;

public class 뒤집기 {
    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Character> stack = new Stack<>();

        String e = sc.nextLine();
        for(int i = 0; i < e.length(); i++){
            if (stack.empty()){
                stack.add(e.charAt(0));
            } else {
                if (stack.lastElement() != e.charAt(i)){
                    stack.add(e.charAt(i));
                }
            }
        }
        int zeroCount = 0;
        for (char ch :stack) {
            if(ch == '0'){
                zeroCount+=1;
            }
        }
        System.out.println(Math.min(stack.size() - zeroCount,zeroCount));
    }
}
