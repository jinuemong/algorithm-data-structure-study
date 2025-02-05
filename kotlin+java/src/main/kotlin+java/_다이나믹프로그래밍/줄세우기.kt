package _다이나믹프로그래밍

fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val n_list = List(n){
        readlnOrNull()?.toInt() ?: return
    }
    val dp = IntArray(n) { 1 }

    for (i in 1 until n) {
        for (j in 0 until i) {
            if (n_list[j] < n_list[i]) {
                dp[i] = maxOf(dp[i], dp[j] + 1)
            }
        }
    }

    println(n-dp.max())
}

// 3 7 5 2 6 1 4
// 1 1 2 1 3 1 1
// 4,7,1,2를 옮김
// 3,5,6은 안옮김
// 3,5,6은 가장 큰 증가하는 부분 수열

