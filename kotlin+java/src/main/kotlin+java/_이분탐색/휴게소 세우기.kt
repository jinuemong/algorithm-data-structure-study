package _이분탐색

fun main() {
    val (n, m, l) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val list = if (n == 0) listOf(0, l)
    else readlnOrNull()?.split(" ")?.map { it.toInt() }?.plus(listOf(0, l))?.sorted() ?: return

    val sections = mutableListOf<Int>()
    for (i in 1 until list.size) {
        sections.add(list[i] - list[i - 1])
    }

    var left = 1
    var right = l
    var answer = l

    while (left <= right) {
        val mid = (left + right) / 2
        var count = 0

        for (sec in sections) {
            count += sec / mid
            if (sec % mid == 0) count--
        }

        if (count > m) {
            left = mid + 1
        } else {
            answer = mid
            right = mid - 1
        }
    }

    println(answer)
}
