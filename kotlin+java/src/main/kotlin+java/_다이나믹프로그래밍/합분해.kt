package _다이나믹프로그래밍
// dp[i][0] = 1
// dp[0][i] = 1
// dp[i][j] = dp[i-1][j] + dp[i][j-1]
fun main() {
    val div = 1_000_000_000
    val (n,k) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val dp = Array(n+1){
        IntArray(k){1}
    }
    for (i in 1..n){
        for (j in 1..k-1){
            dp[i][j] = (dp[i-1][j]+dp[i][j-1])%div
        }
    }
    println(dp[n][k-1]%div)
}

// 0부터 n
// 정수는 k개까지 더할 수 있음
// 1개 2개
// 1 + 2, 2 + 1은 다르다

// 0 20
// 1 19
// 2 18
// 3 17 ... 10개
// 10 10 .. 1개
// 11 9
// 20 0 .. 10개

//dp  1  2  3  4
// 0  1  7
// 1  1  6
// 2  1  5
// 3  1  4
// 4  1  3
// 5  1  2
// 6  1  1
