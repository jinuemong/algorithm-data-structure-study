package _이분탐색
// 과자가 많다
// 이분 탐색을 해야함  -> 정렬 되어있음
// 방안
// 가장 큰 값으로 잘라보기
// 4명에게 나눠줄 수 있다면 채택
// 나눠줄 수 없다면 0
// start = 1
// end = nList.last()
// mid로 쪼갰을 때 인원수보다 많으면 start = mid+1
// mid로 쪼갰을 때 인원수보다 적으면 end = mid
// 끝났을 때 end를 출력하면 됨
fun main() {
    val (m, n) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    val nList = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return

    var start = 1
    var end = nList.maxOrNull() ?: 0
    var mid: Int

    // target 길이에 대해서 나눠줄 수 있는 과자의 개수를 구하는 함수
    fun count(target: Int): Int {
        var count = 0
        for (length in nList) {
            count += length / target
        }
        return count
    }

    while (start <= end) {
        mid = (start + end) / 2
        val current = count(mid)

        if (current >= m) {
            start = mid + 1  // 조카들에게 나눠줄 수 있으면, 더 큰 길이를 시도
        } else {
            end = mid - 1  // 나눠줄 수 없으면, 길이를 줄여야 함
        }
    }

    println(end)  // end가 최적의 길이가 됨
}

// 4 3
// 8로 자를 경우
// 1 1 1
// 10 10 15
// 4명
// 8로 자를 경우
// 8 8 8
// 7로 자를 경우
// 7 7 7 7
// 최악 조건, 최소 조건 찾은 후
// 해당 조건을 중심으로 이분 탐색


