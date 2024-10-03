package _그리디

fun main() {
    val fibo = mutableListOf(0, 1)
    for (i in 2..45) {
        fibo.add(fibo[i - 1] + fibo[i - 2])
    }

    repeat(readlnOrNull()?.toInt() ?: return) {
        var n = readlnOrNull()?.toInt() ?: return
        val result = mutableListOf<Int>()
        for (i in (45 downTo 0)){
            if (n >= fibo[i]){
                n -= fibo[i]
                result.add(fibo[i])
            }

            if (n == 0){
                result.sort()
                println(result.joinToString(" "))
                break
            }
        }
    }
}
