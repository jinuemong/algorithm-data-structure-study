import java.util.*;

public class 자바_기초 {
    public static void main(String[] args) {
        String[] arr1 = new String[5];
        int[] arr2 = {1, 2, 3};

        int N = 3;
        int[] arr3 = new int[N];

        int arr[] = {10, 1, 2, 3, 4};

        Arrays.sort(arr1);
        System.out.println(arr1);
        Arrays.sort(arr1, Collections.reverseOrder());

        Arrays.sort(arr1, 0, 4);

        // 정렬 함수에 대한 search
        Arrays.binarySearch(arr1, 2);

        List<String> list = Arrays.asList(arr1);

        int tmp[] = Arrays.copyOfRange(arr, 0, 3);

        int[] arr4 = new int[3];

        int a = 13;
        int b = 4;
        System.out.println(a + b);

        System.out.println(2.5 + 3.7);

        int i = 0;
        ArrayList<Integer> arrayList = new ArrayList<>();
        Stack<Long> stack = new Stack<>();
        Queue<Float> queue = new ArrayDeque<>();
        ArrayDeque<Double> arrayDeque = new ArrayDeque<>();
        PriorityQueue<Double> priorityQueue = new PriorityQueue<>();
        HashMap<String, Integer> map = new HashMap<>();
        ArrayList<ArrayList<Integer>> arrayList2 = new ArrayList();
        arrayList2.get(2).add(2, 2);
        Arrays.deepToString(arrayList2.toArray());


        int[][] ssssss = new int[5][5];

    }
}
