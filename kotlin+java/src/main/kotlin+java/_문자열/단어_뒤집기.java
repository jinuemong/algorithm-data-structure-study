package _문자열;

import java.util.*;

public class 단어_뒤집기 {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int e = sc.nextInt();
        sc.nextLine();

        for (int i= 0; i<e; i++){
            StringBuilder sb = new StringBuilder();

            String k = sc.nextLine();

            for (int j = 0; j< k.length(); j++){
                if (k.charAt(j) == ' '){
                    System.out.print(sb.reverse());
                    System.out.print(' ');
                    sb.setLength(0);
                }else {
                    sb.append(k.charAt(j));
                }
            }
            System.out.println(sb.reverse());
        }
    }
}
