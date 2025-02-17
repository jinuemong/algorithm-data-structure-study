package _이분탐색
// 연속 부분 수열 ..
// 수가 홀수인 수가 k개 까지 카운트 가능
// 길이가  최대 100만이므로, n이나 logn 사용
fun main() {
    val (n, k) = readln().split(" ").map { it.toInt() }
    val list = readln().split(" ").map { it.toInt() }

    var left = 0
    var oddCount = 0
    var maxEvenLength = 0

    for (right in 0 until n) {
        if (list[right] % 2 == 1) {
            oddCount++
        }

        while (oddCount > k) {
            if (list[left] % 2 == 1) {
                oddCount--
            }
            left++
        }

        maxEvenLength = maxOf(maxEvenLength, right - left + 1 - oddCount)
    }

    println(maxEvenLength)
}
