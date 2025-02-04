package _브루트포스
fun main() {
    val (n, s) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val list = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    var result = 0

    fun dfs(idx: Int, current: Int) {
        if (idx == n) return // 범위를 벗어난 경우 종료

        // 현재 값을 포함한 새로운 합 계산
        val newSum = current + list[idx]

        // 현재 합이 S와 같다면 경우의 수 증가
        if (newSum == s) {
            result += 1
        }

        // 1️⃣ 현재 원소를 선택하는 경우
        dfs(idx + 1, newSum)
        // 2️⃣ 현재 원소를 선택하지 않는 경우
        dfs(idx + 1, current)
    }

    dfs(0, 0) // 첫 번째 원소부터 탐색 시작
    println(result)
}
