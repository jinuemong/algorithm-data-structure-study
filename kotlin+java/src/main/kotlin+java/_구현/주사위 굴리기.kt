package _구현

fun main() {
    val di = listOf(
        0 to 0,  // Dummy index
        0 to 1,  // 동쪽
        0 to -1, // 서쪽
        -1 to 0, // 북쪽
        1 to 0   // 남쪽
    )

    val dice = Array(7) { 0 } // 주사위의 각 면 값을 저장 (1~6)
    var top = 1 // 초기 윗면
    var bottom = 6 // 초기 바닥면
    var north = 2 // 초기 북쪽 면
    var south = 5 // 초기 남쪽 면
    var west = 4 // 초기 서쪽 면
    var east = 3 // 초기 동쪽 면

    var (n, m, x, y, k) = readln().split(" ").map { it.toInt() }
    val graph = Array(n) { readln().split(" ").map { it.toInt() }.toIntArray() }
    val commands = readln().split(" ").map { it.toInt() }

    for (command in commands) {
        val (dx, dy) = di[command]
        val nx = x + dx
        val ny = y + dy

        if (nx in 0 until n && ny in 0 until m) {
            // 주사위를 이동
            when (command) {
                1 -> { // 동쪽
                    val temp = top
                    top = west
                    west = bottom
                    bottom = east
                    east = temp
                }
                2 -> { // 서쪽
                    val temp = top
                    top = east
                    east = bottom
                    bottom = west
                    west = temp
                }
                3 -> { // 북쪽
                    val temp = top
                    top = south
                    south = bottom
                    bottom = north
                    north = temp
                }
                4 -> { // 남쪽
                    val temp = top
                    top = north
                    north = bottom
                    bottom = south
                    south = temp
                }
            }

            // 이동 완료 후, 좌표 갱신
            x = nx
            y = ny

            // 지도와 주사위 바닥값 동기화
            if (graph[x][y] == 0) {
                graph[x][y] = dice[bottom]
            } else {
                dice[bottom] = graph[x][y]
                graph[x][y] = 0
            }

            // 윗면 값 출력
            println(dice[top])
        }
    }
}
