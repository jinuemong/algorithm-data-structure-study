package _백트래킹

fun main() {
    // 증가하는 수열 ?
    // 한개의 모음, 두개의 자음으로 구성
    val mo = setOf("a", "e", "i", "o", "u")
    val (l, c) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val alpha = readlnOrNull()?.split(" ")?.sorted() ?: return

    fun dfs(idx : Int, current: List<String>) {
        if (current.size == l) {
            val moCount = current.count {
                it in mo
            }
            if (moCount >= 1 && current.size - moCount >= 2) {
                println(current.joinToString(""))
            }
            return
        }

        if (c - (idx + 1) < l - current.size) return

        for (i in idx+1..alpha.lastIndex){
            dfs(i,current+alpha[i])
        }
    }
    dfs(-1,listOf())
}
