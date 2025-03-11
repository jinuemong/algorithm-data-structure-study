package _그리디

fun main() {
    val n = readln().toInt()
    val sticks = List(n) { readln().toInt() }.sortedDescending()

    for (i in 0 until n - 2) {
        if (sticks[i] < sticks[i + 1] + sticks[i + 2]) {
            println(sticks[i] + sticks[i + 1] + sticks[i + 2])
            return
        }
    }
    println(-1)
}
