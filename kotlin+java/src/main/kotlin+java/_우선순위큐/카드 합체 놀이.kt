package _우선순위큐

import java.util.PriorityQueue

// 시간 복잡도 : O(mlog n)
// 공간 복잡도 : O(n)
fun main() {
    val (_, m) = readlnOrNull()
        ?.split(" ")
        ?.map { it.toInt() }
        ?: return
    val queue = PriorityQueue(
        readlnOrNull()
            ?.split(" ")
            ?.map { it.toLong()}
            ?: return
    )
    repeat(m){
        val x = queue.poll()
        val y = queue.poll()
        queue.addAll(listOf(x+y,x+y))
    }
    println(queue.sum())
}

// 1 2 3
// 1+2 (1!=2)
// 3 3 3
// -> 9 (최소 만들기)
