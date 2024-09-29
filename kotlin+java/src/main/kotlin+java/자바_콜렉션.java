import java.util.*;

public class 자바_콜렉션 {
    public void main(String [] args){
        Integer [] temp = {1,23,12,4,5};
        List<Integer> list = new ArrayList<>(Arrays.asList(temp));

        Collections.max(list);
        Collections.min(list);

        Collections.reverse(list);;

        // 원소 수 반환
        Collections.frequency(list,3);

        // 이진 탐색 후 인덱스 반환 -> 정렬 필요
        Collections.binarySearch(list,10);

        // Stack
        Stack<Integer> stack = new Stack<>();

        stack.push(1);

        stack.pop();

        stack.clear();

        stack.size();
        stack.empty();
        stack.contains(1);
        stack.peek();

        // Queue
        Queue<Integer> queue = new LinkedList<>();

        queue.add(1);
        queue.offer(2); // false

        queue.remove();
        queue.poll(); // 없을 시 null 반화

        queue.clear();

        queue.element(); //최전방 요소 확인
        queue.peek(); // 문제 시 null 발생


        // Hash
        HashSet<Integer> hashSet = new HashSet<>();
        HashSet<Integer> hashSet2 = new HashSet<>();

        // 차집합
        hashSet.removeAll(hashSet2);

        // 교집합
        hashSet2.retainAll(hashSet2);

        // 데이터 초기화
        hashSet2.clear();

        hashSet2.size();

        hashSet2.contains(1);

        // 요소 전체 출력
        Iterator tempIterator = hashSet.iterator();
        while (tempIterator.hasNext()){
            System.out.println(tempIterator.next());
        }

        for (Integer item : hashSet2){
            System.out.println(item);
        }

        HashMap<Integer, String> hashMap = new HashMap<>();

        hashMap.put(1,"dd");
        hashMap.put(2,"22");

        hashMap.remove(1);

        hashMap.clear();

        hashMap.containsKey(1);

        hashMap.containsValue("dd");

        for (Integer key : hashMap.keySet()){
            System.out.println(key + " "+ hashMap.get(key));
        }

        for (Map.Entry<Integer,String> temp3 : hashMap.entrySet()){
            System.out.println(temp3.getKey() + " " + temp3.getValue());
        }
    }
}
