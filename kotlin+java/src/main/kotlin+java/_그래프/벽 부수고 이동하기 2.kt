package _그래프

data class Man2(val spot : Pair<Int,Int>,val count: Int, val stone : Int)

fun main() {
    val di = listOf(
        0 to 1,
        0 to -1,
        1 to 0,
        -1 to 0
    )
    val (n,m,k) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val graph = List(n){
        readlnOrNull()?.map{it.digitToInt()} ?: return
    }
    // k개의 벽을 부쉈을 때의 가중치
    val dp = Array(n){
        Array(m){
            IntArray(k+1){Int.MAX_VALUE}
        }
    }

    val que = ArrayDeque<Man2>()
    que.add(Man2(0 to 0, 1, 0))
    dp[0][0][0] = 1

    while(que.isNotEmpty()){
        val man = que.removeFirst()
        if (man.spot.first == n-1 && man.spot.second == m-1) continue
        val canBroken = man.stone < k
        for ((dx,dy) in di){
            val (nx,ny) = dx+man.spot.first to dy+man.spot.second
            if (nx !in 0..<n || ny !in 0..<m) continue
            val isWall = graph[nx][ny] == 1
            val nextCount = man.count + 1
            val nextStone = man.stone + 1
            val currentStone = man.stone
            if (isWall && canBroken && nextCount <dp[nx][ny][nextStone]){
                val brokenMan = Man2(nx to ny, nextCount,nextStone)
                dp[nx][ny][nextStone] = nextCount
                que.add(brokenMan)
            }

            if (!isWall && nextCount < dp[nx][ny][currentStone]){
                val nextMan = Man2(nx to ny, nextCount,currentStone)
                dp[nx][ny][currentStone] = nextCount
                que.add(nextMan)
            }
        }
    }

    val result = dp[n-1][m-1].min()
    if (result== Int.MAX_VALUE){
        println(-1)
    }else{
        println(result)
    }
}
