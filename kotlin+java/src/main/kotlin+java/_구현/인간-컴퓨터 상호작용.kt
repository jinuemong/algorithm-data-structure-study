package _구현

fun main() {
    val s = readlnOrNull() ?: return
    val dp = List(s.length) {
        IntArray(26) { 0 }
    }
    dp[0][s[0].toInt() - 97] = 1
    for (idx in 1..s.lastIndex) {
        val num = s[idx].toInt() - 97
        for (i in 0..<26) {
            dp[idx][i] = dp[idx - 1][i]
        }
        dp[idx][num] += 1
    }

    repeat(readlnOrNull()?.toInt() ?: return) {
        val (a, l, r) = readlnOrNull()
            ?.split(" ")
            ?: return
        val code = a[0].toInt() - 97
        val left = l.toInt()
        val right = r.toInt()
        val countAtRight = dp[right][code]
        val countAtLeft = if (left > 0) dp[left - 1][code] else 0
        println(countAtRight - countAtLeft)
    }
}

//   a,b,c,d.....z
//0
//1
//2
//3
//4
// ..s.lastIndex
