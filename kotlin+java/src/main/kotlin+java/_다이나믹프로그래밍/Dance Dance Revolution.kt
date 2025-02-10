package _다이나믹프로그래밍
// 중앙 -> 다른 지점 2
// 다른 지점 -> 인접 지점 3 (두 수의 차이가 1)
// 다른 지점 -> 반대편 4 (두 수의 차이가 2)
import java.util.PriorityQueue

data class Game(val left: Int, val right: Int, val idx: Int, val w: Int)

fun main() {
    val list = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return

    val weight = arrayOf(
        intArrayOf(0, 2, 2, 2, 2),
        intArrayOf(0, 1, 3, 4, 3),
        intArrayOf(0, 3, 1, 3, 4),
        intArrayOf(0, 4, 3, 1, 3),
        intArrayOf(0, 3, 4, 3, 1),
    )

    val INF = Int.MAX_VALUE
    // dp[left][right][idx] idx까지 진행했을 때의 left,right 상태의 최소 힘
    val dp = Array(5) { Array(5) { IntArray(list.size + 1) { INF } } }
    val que = PriorityQueue<Game>(compareBy { it.w })

    que.add(Game(0, 0, 0, 0))
    dp[0][0][0] = 0

    while (que.isNotEmpty()) {
        val game = que.poll()

        if (game.idx == list.size) {
            println(game.w)
            return
        }

        val current = list[game.idx]

        // 왼발 이동
        if (game.right != current) { // 두 발이 같은 위치가 되면 안 됨
            val newCost = game.w + weight[game.left][current]
            if (newCost < dp[current][game.right][game.idx + 1]) {
                dp[current][game.right][game.idx + 1] = newCost
                que.add(Game(current, game.right, game.idx + 1, newCost))
            }
        }

        // 오른발 이동
        if (game.left != current) { // 두 발이 같은 위치가 되면 안 됨
            val newCost = game.w + weight[game.right][current]
            if (newCost < dp[game.left][current][game.idx + 1]) {
                dp[game.left][current][game.idx + 1] = newCost
                que.add(Game(game.left, current, game.idx + 1, newCost))
            }
        }
    }
}
