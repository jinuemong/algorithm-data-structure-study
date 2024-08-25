fun main() = with(System.`in`.bufferedReader()) {
    val integer = readLine().toInt()

    // 공백 기준으로 분리
    val nums = readLine()
        .split(" ")
        .map { it.toInt() }

    print(integer)

    print(nums)

    val sb = StringBuilder()
    sb.append(5)
    sb.append("abc")

    print(sb)

    val bw = System.out.bufferedWriter()
    bw.flush()
    bw.close()
}
