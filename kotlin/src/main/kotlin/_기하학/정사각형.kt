package _기하학

import kotlin.math.pow

fun main() {
    val t = readln().toInt()

    repeat(t) {
        val points = mutableListOf<Pair<Int, Int>>()

        repeat(4) {
            val (x, y) = readln().split(" ").map { it.toInt() }
            points.add(Pair(x, y))
        }

        val distances = mutableListOf<Int>()
        for (i in 0 until 4) {
            for (j in i + 1 until 4) {
                val d = distanceSquared(points[i], points[j])
                distances.add(d)
            }
        }

        distances.sort()

        if (distances[0] == distances[1] &&
            distances[1] == distances[2] &&
            distances[2] == distances[3] &&
            distances[4] == distances[5] &&
            distances[0] != distances[4]
        ) {
            println(1)
        } else {
            println(0)
        }
    }
}

fun distanceSquared(p1: Pair<Int, Int>, p2: Pair<Int, Int>): Int {
    return (p2.first - p1.first).toDouble().pow(2).toInt() + (p2.second - p1.second).toDouble().pow(2).toInt()
}
