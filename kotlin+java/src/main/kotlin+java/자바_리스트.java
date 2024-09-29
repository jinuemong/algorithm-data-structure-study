
import java.util.*;

public class 자바_리스트 {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        List<String> list2 = new ArrayList<>();

        list.add("one");

        list.add(0,"one");

        list.addAll(list2);

        list.indexOf("zero"); //첫 요소 반환, 없을 시 -1

        list.lastIndexOf("zero");

        list.remove(0);

        list.remove("one");

        //차집합
        list.removeAll(list2);

        //교집합
        list.retainAll(list2);

        //리스트 비우기
        list.clear();

        list.contains("one");

        // 리스트에 다른 리스트 요소가 전부 포함되어있는지 확인
        list.containsAll(list2);

        // Array
        // ArrayList는 변경 불가능
        String[] temp = {"apple","banana","lemon"};
        List<String> arrayList = new ArrayList<>(Arrays.asList(temp));

        // List를 문자열 배열로 전환
        List<String> arrayList2 = new ArrayList<>();
        String[] tem = arrayList2.toArray(new String[arrayList2.size()]);

        // 정수 배열을 List로 치환
        Integer[] temp2 = {1,2,3,4};
        List<Integer> list3 = new ArrayList<>(Arrays.asList(temp2));

        // List를 정수 배열로 변환
        List<Integer> list4 = new ArrayList<>();
        int[] temp4 = list4.stream().mapToInt(x ->x).toArray();
    }
}

