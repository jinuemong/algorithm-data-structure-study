package _다이나믹프로그래밍
fun main(){
    val n = readlnOrNull()?.toInt() ?: return
    val dp = Array(n+1){0L}
    if(n==1) return println(1)
    if(n==2) return println(2)
    dp[1] = 1
    dp[2] = 2

    for(i in 3..n){
        dp[i] = (dp[i-1] + dp[i-2])%10007
    }
    println(dp[n])
}

// 2  * 1
// 1
// 2 * 2
// 2
// 2*3
// 3
// 2*4
//

// [] [] [] []
// [] [] [] []
// 3 +
