package _문자열
fun main() {
    val st = readlnOrNull() ?: return
    val n = st.length
    val result = mutableListOf<String>()

    for (i in 1 until n - 1) {
        for (j in i + 1 until n) {
            val part1 = st.substring(0, i).reversed()
            val part2 = st.substring(i, j).reversed()
            val part3 = st.substring(j).reversed()
            val newWord = part1 + part2 + part3
            result.add(newWord)
        }
    }

    println(result.min())
}
