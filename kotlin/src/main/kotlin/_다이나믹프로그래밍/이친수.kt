package _다이나믹프로그래밍

fun main() {
    val n = readLine()?.toInt() ?: return
    val dp = Array(n+1){0L}
    dp[1] = 1
    for (i in 2..n){
        dp[i] = dp[i-1] + dp[i-2]
    }
    println(dp[n])
}
