package _다이나믹프로그래밍
// 디폴트 : i번째 집은 i-1, i+1 집의 색과 달라야 함
// 1번 집은 2번, n번 집의 색과 달라야 함
// n번 집은 1번, n-1번 집의 색과 달라야 함
// 마지막 인덱스가 연결 된 dp
// n번집을 기준으로 잡을지, 1번집을 기준으로 잡을 지 선택
fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val maxValue = 1001
    val rgb = List(n){
        readlnOrNull()?.split(" ")?.map{it.toInt() } ?: return
    }
    var result = Int.MAX_VALUE
    // 0 : r, 1 : g, 2 : b
    for (i in 0..<3){
        val dp = Array(n){
            arrayOf(maxValue,maxValue,maxValue)
        }
        dp[0][i] = rgb[0][i]
        for (j in 1..<n){
            // r 선택
            dp[j][0] = rgb[j][0] + minOf(dp[j-1][1],dp[j-1][2])
            // g 선택
            dp[j][1] = rgb[j][1]+ minOf(dp[j-1][0],dp[j-1][2])
            // b 선택
            dp[j][2] = rgb[j][2] + minOf(dp[j-1][0],dp[j-1][1])
        }
        for (j in 0..<3){
            // 처음으로 선택한 값과 달라야 함
            if (i!=j){
                result = minOf(result,dp[n-1][j])
            }
        }
    }
    println(result)
}

//[g,b] [r,b] [r,g]
// r      g     b
// 26     40    83
//[g,b] [r,b] [r,g]

// [g]  [r,b] [r,g]
// [r]   g     b
// [b] [r,b]  [r,g]
