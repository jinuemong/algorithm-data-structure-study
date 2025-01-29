package _그리디

fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val words = List(n) {
        readlnOrNull() ?: return
    }.sortedBy {
        it.length
    }
    val result = BooleanArray(n) { true }

    for (i in 0..words.lastIndex - 1) {
        val current = words[i]
        for (j in i + 1..words.lastIndex) {
            if (!result[i]) continue
            if (current == words[j].substring(0, current.length)) {
                result[i] = false
            }
        }
    }
    println(result.count { it })
}
