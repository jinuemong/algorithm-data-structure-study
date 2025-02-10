package _그래프

// 벽은 낮에만 부술 수 있다
data class Man(val x: Int, val y: Int, val count: Int, val life: Int)
// 벽을 몇개 부수고 이동했는지 확인해야 할듯
// 이동하지 않고 방에 머무는 경우 -> 밤이라 못부수니까 낮까지 기다리기 ! -> count + 1
// 즉 + 2 인 경우로 벽을 부수고 가는 경우가 더 짧다면 이동이 가능

fun main() {
    val di = listOf(
        0 to 1,
        0 to -1,
        1 to 0,
        -1 to 0,
    )

    val (n, m, k) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val graph = List(n) {
        readlnOrNull()?.map { it.digitToInt() } ?: return
    }

    val end = n - 1 to m - 1
    val que = ArrayDeque<Man>()

    // k번째 벽을 부술때까지의 기록
    val dp = Array(n) {
        Array(m) {
            IntArray(k + 1) { Int.MAX_VALUE }
        }
    }
    // 낮에서 시작
    dp[0][0][0] = 1
    que.add(Man(0, 0, 1, 0))
    var result =  Int.MAX_VALUE
    while (que.isNotEmpty()) {
        val man = que.removeFirst()

        if (man.x == end.first && man.y == end.second){
            result = minOf(result,man.count)
            continue
        }

        val isMorning = man.count % 2 == 1
        val isLife = man.life < k

        for ((dx, dy) in di) {
            val (nx, ny) = dx + man.x to dy + man.y
            if (nx in 0..<n && ny in 0..<m) {
                val isWall = graph[nx][ny] == 1
                // 벽을 부수고 이동
                if (isWall && isLife) {
                    val nextLife = man.life + 1
                    // 낮이라 벽을 부수고 이동
                    // 벽을 부순 횟수가 k보다 작아야 함
                    if (isMorning) {
                        if (man.count + 1 < dp[nx][ny][nextLife]) {
                            val brokenMan = Man(nx, ny, man.count + 1, nextLife)
                            que.add(brokenMan)
                            dp[nx][ny][nextLife] = brokenMan.count
                        }
                        // 밤이라 하루 기다리고 벽을 부수고 이동
                    } else {
                        if (man.count+2 < dp[nx][ny][nextLife]){
                            val brokenMan = Man(nx, ny, man.count + 2, nextLife)
                            que.add(brokenMan)
                            dp[nx][ny][nextLife] = brokenMan.count
                        }
                    }
                }

                // 벽이 아닌 경우 그냥 이동
                if (!isWall && man.count + 1 < dp[nx][ny][man.life]) {
                    val nextMan = Man(nx, ny, man.count + 1, man.life)
                    que.add(nextMan)
                    dp[nx][ny][man.life] = nextMan.count
                }
            }
        }
    }
    // 이동 불가능
    if (result == Int.MAX_VALUE) {
        println(-1)
    } else {
        println(result)
    }
}
