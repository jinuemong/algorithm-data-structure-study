package _그리디
// 같은 양의 물 병은 하나로 합치기


fun main() {
    val (n,k) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val dp = IntArray(32)
    if (n<=k) return println(0)
    dp[0] =  n
    var count =  n
    var result = 0
    while (true){
        count = 0
        for (i in 0..30){
            dp[i+1] += dp[i]/2
            dp[i] = dp[i]%2
            count+=dp[i]
        }

        if (count <= k) break
        if (dp[0]%2 == 0){
            dp[0]+=2
            result+=2
        }else {
            dp[0]+=1
            result+=1
        }
    }
    println(result)

}

// 1 1 1 (1) 구매
// 2 1 1
// 2 2
// 4

// 13

