package _그리디

import java.util.PriorityQueue

fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val first = readlnOrNull()?.toInt() ?: return
    val que = PriorityQueue<Int>(
        compareBy { -it }
    )
    if (n==1) return println(0)
    repeat(n-1){
        que.add(readlnOrNull()?.toInt() ?: return)
    }
    var my = first
    while (que.peek() >= my){
        val current = que.poll()
        my++
        que.add(current-1)
    }
    println(my-first)
}
