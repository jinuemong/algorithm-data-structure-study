package _이분탐색
fun main() {
    repeat(readlnOrNull()?.toInt() ?: return) {
        val n = readlnOrNull()?.toInt() ?: return
        val li = readlnOrNull()?.split(" ")?.map { it.toInt() }?.sorted() ?: return

        val arranged = IntArray(n)
        var left = 0
        var right = n - 1
        // 짝수면 왼쪽, 홀수면 오른쪽 배치
        for (i in li.indices) {
            if (i % 2 == 0) {
                arranged[left++] = li[i]
            } else {
                arranged[right--] = li[i]
            }
        }

        var maxDiff = 0
        for (i in 1 until n) {
            maxDiff = maxOf(maxDiff, kotlin.math.abs(arranged[i] - arranged[i - 1]))
        }
        // 양방향 고려
        maxDiff = maxOf(maxDiff, kotlin.math.abs(arranged[0] - arranged[n - 1]))

        println(maxDiff)
    }
}

// 13 10 12 11 10 11 12
// 10 11 12 /13/ 12 11 10 -> 1
// 10 11 12 / 13 12 11 -> 1
// 2 4 5 7 9
// 2 5 9 7 4
// 13 10 12 11 10 11 12
// 10 10 11 11 12 12 13
// 10 11 12 13 12 11 10


// 1
