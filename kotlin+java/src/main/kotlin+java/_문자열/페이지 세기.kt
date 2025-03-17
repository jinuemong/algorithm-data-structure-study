package _문자열

fun main() {
    while (true) {
        val n = readlnOrNull()?.toInt() ?: return
        if (n == 0) return

        val input = readlnOrNull() ?: return
        val pages = mutableSetOf<Int>()

        val regex = """(\d+)-(\d+)|(\d+)""".toRegex()

        for (match in regex.findAll(input)) {
            if (match.groups[1] != null) { // low-high 형태
                val low = match.groups[1]!!.value.toInt()
                val high = match.groups[2]!!.value.toInt()
                if (low <= high) {
                    for (i in low..minOf(high, n)) {
                        pages.add(i)
                    }
                }
            } else if (match.groups[3] != null) { // 단일 숫자
                val num = match.groups[3]!!.value.toInt()
                if (num in 1..n) {
                    pages.add(num)
                }
            }
        }

        println(pages.size)
    }
}
