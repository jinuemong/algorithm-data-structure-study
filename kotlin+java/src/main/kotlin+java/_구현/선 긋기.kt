package _구현

fun main() {
    val n = readLine()?.toInt() ?: return

    val nList = List(n) {
        readLine()?.split(" ")?.map { it.toInt() } ?: return
    }.sortedBy { it[0] }

    var result = 0
    var (start, end) = -1_000_000_001 to -1_000_000_001

    for (i in 0 until nList.size) {
        val current = nList[i]
        if (current[0] <= end) {  // 겹치는 구간이 있을 경우
            end = maxOf(end, current[1])  // end 값을 확장
        } else {  // 겹치지 않는 경우
            result += end - start  // 이전 구간의 길이 추가
            start = current[0]
            end = current[1]
        }
    }
    result += end - start  // 마지막 구간의 길이 추가
    println(result)
}

// 1 2 3 4 5 6 7
// x x x
//   x x x x
//     x x x
//           x x
