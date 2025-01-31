package _최단경로

import java.util.PriorityQueue
fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val st = Array(n) {
        readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    }.sortedWith(
        compareBy(
            {it[0]},
            {it[1]}
        )
    )
    val queue = PriorityQueue<Int>()
    queue.add(st[0][1])
    for ( i in 1..st.lastIndex){
        if (queue.first() <= st[i][0]) queue.poll()
        queue.add(st[i][1])
    }
    println(queue.size)
}

// 최소의 강의실 사용 -> 최대한 겹치는 강의 활용
// 끝나는 시간을 저장해서 활용
// 1 3
// 2 4
// 3 5


