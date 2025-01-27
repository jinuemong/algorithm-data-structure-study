package _그래프

import kotlin.math.abs

fun main() {
    val t = readlnOrNull()?.toInt() ?: return
    repeat(t) {
        val n = readlnOrNull()?.toInt() ?: return
        val (sx, sy) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        val shop = mutableListOf<Pair<Int, Int>>()
        repeat(n) {
            val (x, y) = readlnOrNull()?.split(" ")?.map(String::toInt) ?: return
            shop.add(x to y)
        }
        val (lx, ly) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return

        val deque = ArrayDeque<Pair<Int, Int>>()
        deque.add(sx to sy)
        val visited = mutableSetOf<Pair<Int, Int>>()

        var isHappy = false
        while (deque.isNotEmpty()) {
            val (cx, cy) = deque.removeFirst()

            // 목적지에 도달 가능한지 확인
            if (abs(lx - cx) + abs(ly - cy) <= 1000) {
                isHappy = true
                break
            }

            // 편의점 탐색
            shop.forEach {
                if (it !in visited && abs(it.first - cx) + abs(it.second - cy) <= 1000) {
                    visited.add(it)
                    deque.add(it)
                }
            }
        }

        println(if (isHappy) "happy" else "sad")
    }
}
