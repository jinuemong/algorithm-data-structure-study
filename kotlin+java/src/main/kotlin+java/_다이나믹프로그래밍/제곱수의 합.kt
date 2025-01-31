package _다이나믹프로그래밍

fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val dp = IntArray(n+1){it} // 1제곱수의 합으로 정의

    for (i in 1..n){
        var j = 1
        while (j*j <= i) {
            dp[i] = minOf(dp[i],dp[i-j*j]+1)
            j++
        }
    }
    println(dp.last())
}
//dp 0 1 2 3 4 5
//i = 2
//i = 3
//i = 4
//i = 5

