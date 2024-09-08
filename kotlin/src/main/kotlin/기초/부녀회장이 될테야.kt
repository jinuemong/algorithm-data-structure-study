package 기초

fun main() = with(System.`in`.bufferedReader()) {
    repeat(readLine().toInt()) {
        val k = readLine().toInt()
        val n = readLine().toInt()
        val dp = Array(k+1){
            IntArray(n+1){
                it
            }
        }
        for (i in 1..k){
            for (j in 1..n){
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
            }
        }
        println(dp[k][n])
    }
}
