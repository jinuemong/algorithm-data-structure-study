package 기초

fun main() = with(System.`in`.bufferedReader()) {
    val (a, b, c) = readln()
        .split(" ")
        .map { it.toLong() }
    print(a + b + c)
}
