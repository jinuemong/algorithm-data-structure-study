package _그리디

fun main() {
    var (n, k) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    var result = 0
    val coin = List(n) {
        readlnOrNull()?.toInt() ?: return
    }

    coin.reversed().forEach {
        val count = k / it
        if (count > 0) {
            result += count
            k %= it
        }
    }
    println(result)

}
