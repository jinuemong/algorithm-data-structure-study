fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val home = readlnOrNull()?.split(" ")?.map { it.toInt() }?.sorted() ?: return

    // 중앙값 찾기
    val medianIndex = (n - 1) / 2
    println(home[medianIndex])
}
//fun main() {
//    val n = readlnOrNull()?.toInt() ?: return
//    val home = readlnOrNull()?.split(" ")?.map{it.toInt()}?.sorted() ?: return
//    val dp = Array(n+1){
//        IntArray(n+1)
//    }
//    for (i in 2..n){
//        val current =  home[i-1] - home[0]
//        dp[1][i] = current
//        dp[i][1] = current
//
//    }
//    for (i in 2..n){
//        for (j in i+1..n){
//            val current = dp[i-1][j] - dp[i-1][i]
//            dp[i][j] = current
//            dp[j][i] = current
//        }
//    }
//    var result = Int.MAX_VALUE
//    var answer  = Int.MAX_VALUE
//    for ( i in 1..n){
//        val current = dp[i].sum()
//        if (current < result){
//            result = current
//            answer = minOf(home[i],answer)
//        }
//    }
//    println(answer)
//}
//
