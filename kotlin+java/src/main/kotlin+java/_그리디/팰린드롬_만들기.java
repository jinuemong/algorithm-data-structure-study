package _그리디;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class 팰린드롬_만들기 {
    public static void main(String[] args) {
        String defailt_string = "I'm Sorry Hansoo";
        Scanner sc = new Scanner(System.in);
        Map<Character, Integer> hashMap = new HashMap<>();

        String s = sc.nextLine();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            int value = hashMap.getOrDefault(ch, 0);
            hashMap.put(ch, value + 1);
        }
        int hallCount = 0;
        StringBuilder sb = new StringBuilder();
        Character center = ' ';
        Map<Character,Integer> sortedMap = new TreeMap<>(hashMap);
        for (Map.Entry<Character,Integer> entry : sortedMap.entrySet()){
            if (entry.getValue()%2 == 1){
                hallCount+=1;
                center = entry.getKey();
            }
            for (int i = 0; i < (entry.getValue())/2; i++){
                sb.append(entry.getKey());
            }
        }

        boolean flag = true;
        if (hallCount == 1) {
            if (s.length() % 2 == 0) {
                flag = false;
            }
        } else if (hallCount > 1) {
            flag = false;
        }
        if (flag) {
            if (center.equals(' ')){
                System.out.print(sb);
                System.out.println(sb.reverse());
            }else {
                System.out.print(sb);
                System.out.print(center);
                System.out.println(sb.reverse());
            }
        } else {
            System.out.println(defailt_string);
        }

    }
}
