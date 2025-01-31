package _다이나믹프로그래밍
fun main(){
    val t= readlnOrNull()?.toInt() ?: return
    val nList = List(t){
        readlnOrNull()?.toInt() ?: return
    }
    val maxValue = nList.max()
    val dp = LongArray(maxValue+1){ it.toLong() }
    if (maxValue>=1) dp[1] = 1
    if (maxValue>=2) dp[2] = 2
    if (maxValue>=3) dp[3] = 4
    for (i in 4..maxValue){
        dp[i]= (dp[i-1]+dp[i-2]+dp[i-3]) % 1_000_000_009
    }

    nList.forEach {
        println(dp[it])
    }
}

// 1 = 1 => 1
// 2 = 1+1, 2 => 2
// 3 = 1+1+1, 1+2, 2+1, 3 => 4
// 4 => 7
//
// 5 =>  13
// 6 =>
// 1+1+1+1+1
// 2+1+1+1, 1+2+1+1, 1+1+2+1, 1+1+1+2
// 2+2+1, 2+1+2, 1+2+2
// 3+1+1, 1+3+1, 1+1+3
// 3+2, 2+3
// 7 => 44
