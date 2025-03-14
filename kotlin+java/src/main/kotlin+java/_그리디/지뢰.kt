package _그리디
import java.util.*

fun findMinExplosions(n: Int, mines: List<Int>): List<Int> {
    val visited = BooleanArray(n)
    val result = mutableListOf<Int>()
    val pq = PriorityQueue<Pair<Int, Int>>(compareByDescending<Pair<Int, Int>> { it.first }.thenBy { it.second })

    for (i in mines.indices) {
        pq.add(mines[i] to i)
    }

    var explodedCount = 0

    while (pq.isNotEmpty()) {
        val (_, index) = pq.poll()
        if (visited[index]) continue

        result.add(index + 1)
        val queue: Queue<Pair<Int, Int>> = LinkedList()
        queue.add(index to mines[index])
        visited[index] = true
        explodedCount++

        while (queue.isNotEmpty()) {
            val (idx, power) = queue.poll()

            var leftIdx = idx - 1
            var leftPower = power
            while (leftIdx >= 0 && !visited[leftIdx] && leftPower > mines[leftIdx]) {
                queue.add(leftIdx to mines[leftIdx])
                visited[leftIdx] = true
                explodedCount++
                leftPower = mines[leftIdx]
                leftIdx--
            }

            var rightIdx = idx + 1
            var rightPower = power
            while (rightIdx < n && !visited[rightIdx] && rightPower > mines[rightIdx]) {
                queue.add(rightIdx to mines[rightIdx])
                visited[rightIdx] = true
                explodedCount++
                rightPower = mines[rightIdx]
                rightIdx++
            }
        }

        if (explodedCount == n) break
    }

    return result.sorted()
}

fun main() {
    val n = readLine()!!.toInt()
    val mines = List(n) { readLine()!!.toInt() }
    val result = findMinExplosions(n, mines)
    result.forEach { println(it) }
}

// 1 2 5 4 3 3 6 6 2
// 0 0 0 0 0 0 0 0 0
// 1 2 5 2 1 1 2 2 1
//
// 9개 선택
// 2번 선택 -> -1
// 3번 선택 -> -4
