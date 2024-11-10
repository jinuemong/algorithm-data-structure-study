import java.util.LinkedList
import java.util.PriorityQueue
import kotlin.collections.ArrayDeque

fun main() {
    // 배열 쉽게 생성
    val arr1 = intArrayOf(1, 2, 3)

    val arr2 = IntArray(4) { 0 }
    val arr3 = IntArray(4) { it * 2 } //it = index
    print(arr3.contentToString())

    // 다차원 배열
    val n = 2
    val m = 3
    val arr4 = Array(n) {
        BooleanArray(m)
    }
    arr4[0][0] = true
    println(arr4[0][0])

    // 리스트

    // 불변 리스트
    val list1 = listOf(1, 2, 3)
    val list2 = mutableListOf(1, 2, 3)

    // 가변 리스트
    val list3 = List<Int>(5) { 0 }

    // 스택
    // 별도의 스택 클래스가 존재하지 않음
    val stack = MutableList<Int>(4) { it } // 인덱스

    stack.add(5) // push
    stack.removeLast() // pop
    stack.last() // peek

    stack.isEmpty()
    stack.isNotEmpty()

    // 큐
    val q = LinkedList<Int>()
    q.offer(3) // push
    q.peek() // peak
    q.poll() // pop

    // 덱 deque
    val deque = ArrayDeque<Int>()

    deque.addLast(1)
    deque.add(2)

    deque.removeFirst()
    deque.removeLast()

    deque.first()
    deque.last()

    // priorityQueue
    // 우선순위가 높은 최대 힙
    val a = PriorityQueue<Int>()

    a.addAll(arrayOf(1,5,67,85,3,4)) // 생성
    a.offer(111) // 단일 추가

    println(a.peek()) // 가장 높은 우선순위 출력
    println(a.poll()) // 가장 높은 우선순위 pop

    val b = PriorityQueue<String> { a,b ->
        // 커스텀으로, a와 b를 비교할 때 길이를 통해 정렬한다
        a.length.compareTo(b.length)
    }
    b.addAll(arrayOf("sdf","123123","23424","z"))
    println(b) // [z,sdf,23424,123123]

}
