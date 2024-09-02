package 기초

// 대각선  = 루트 a**2 + b**2
fun main() = with(System.`in`.bufferedReader()) {
    val t = readLine().toInt()
    repeat(t) {
        val (a, b, c) = readLine()
            .split(" ")
            .map { it.toLong() }
        val answer = minOf(
            (a * a) + (b + c) * (b + c),
            (b * b) + (a + c) * (a + c),
            (c * c) + (a + b) * (a + b),
        )
        println(answer)
    }
}

