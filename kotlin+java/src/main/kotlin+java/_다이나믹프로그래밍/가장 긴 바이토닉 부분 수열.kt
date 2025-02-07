package _다이나믹프로그래밍
fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val nm = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val dp = Array(n) { 1 }
    val reDp = Array(n) { 1 }

    for (i in 1..<n){
        for (j in 0..<i){
            if (nm[i]>nm[j]){
                dp[i] = maxOf(dp[i],dp[j]+1)
            }
        }
    }

    for (i in n-2 downTo 0){
        for ( j in n-1 downTo i+1){
            if (nm[i]>nm[j]){
                reDp[i] = maxOf(reDp[i],reDp[j]+1)
            }
        }
    }
    var result = 0
    for (i in 0..<n){
        result = maxOf(result,dp[i]+reDp[i]-1)
    }
    println(result)
}

//     1 5 2 1 4 3
// dpi
// i=1 1
// i=2

// 가장 긴 증가하는 수열 ->
// 가장 긴 증가하는 수열 <-

