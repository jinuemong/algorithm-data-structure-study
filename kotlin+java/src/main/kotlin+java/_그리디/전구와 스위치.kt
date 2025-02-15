package _그리디
// 풀이 방법 : 첫 전구를 누르는가?
// 첫 전구를 기준으로 가지 탐색
// 이 후부터는 이전 전구를 목표와 다르지 않게 하도록 눌러가며 선택과 비선택 반복
// 최종 도착했을 때 다르면 만들수 없음 !

fun main() {
    val n = readln().toInt()
    val current = readln().map { it - '0' }.toIntArray()
    val goal = readln().map { it - '0' }.toIntArray()

    fun toggle(arr: IntArray, index: Int) {
        for (i in index - 1..index + 1) {
            if (i in arr.indices) arr[i] = arr[i] xor 1
        }

    }

    fun solve(startToggle: Boolean): Int {
        val bulbs = current.copyOf()
        var count = 0

        if (startToggle) {
            toggle(bulbs, 0)
            count++
        }

        for (i in 1 until n) {
            if (bulbs[i - 1] != goal[i - 1]) {
                toggle(bulbs, i)
                count++
            }
        }

        return if (bulbs.contentEquals(goal)) count else Int.MAX_VALUE
    }

    val result = minOf(solve(false), solve(true))
    println(if (result == Int.MAX_VALUE) -1 else result)
}
