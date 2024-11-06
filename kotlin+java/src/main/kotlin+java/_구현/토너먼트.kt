package _구현

fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
    var (N, jimin, hansoo) = readLine().split(" ").map { it.toInt() }
    var count = 0

    while (jimin != hansoo) {
        jimin = jimin / 2 + jimin % 2
        hansoo = hansoo / 2 + hansoo % 2
        count++
    }

    println(count)
}
