//       !     !
// 1 2 3 4 5 6 7 8 9
// 1 2 3 4 5 6 7
//         6 5 7
//   3 2 4 5 6 7
//         6 5 7
// 2 1 3 4 5 6 7
//         6 5 7
// 2 3 3 3 6 6 6
// 다음 수가 VIP이거나 마지막 수이면, 그 수까지 동결
// 그 외는 2가지 경우의 수
fun main() {
    val n = readln().toInt()
    val m = readln().toInt()
    val vip = List(m) { readln().toInt() }

    val dp = IntArray(n + 1) { 0 }
    dp[0] = 1
    dp[1] = 1 // 1
    if (n >= 2) dp[2] = 2 // 1 2, 2 1

    // dp 배열 초기화
    for (i in 3..n) {
        dp[i] = dp[i - 1] + dp[i - 2]
    }

    var answer = 1
    if (m > 0) {
        var pre = 0
        for (j in vip.indices) {
            answer *= dp[vip[j] - 1 - pre]
            pre = vip[j]
        }
        answer *= dp[n - pre]
    } else {
        answer = dp[n]
    }

    println(answer)
}


