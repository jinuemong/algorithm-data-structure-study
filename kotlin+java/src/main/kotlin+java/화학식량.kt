// H : 1, C : 12, O : 16
fun main() {
    fun value(c: Char): Int {
        return when (c) {
            'H' -> 1
            'C' -> 12
            'O' -> 16
            else -> 0
        }
    }

    var result = 0
    val st = readlnOrNull()?.reversed() ?: return
    var ct = 1
    var temp = 1 // 문자 바로 옆 숫자
    val stack = mutableListOf<Int>()
    //  )만나면 stack에 추가하고 ct에 곱
    // (만나면 stack에서 제거하고 ct 나누기
    // 숫자 만나면 다음이 괄호라면 stack에 추가, 다음이 문자라면 임시 저장
    st.forEach {
        when (it) {
            in "123456789" -> {
                temp = it.digitToInt()
            }

            ')' -> {
                stack.add(temp)
                ct *= temp
                temp = 1
            }

            '(' -> {
                if (stack.isNotEmpty()) {
                    val re = stack.removeLast()
                    ct /= re
                }
            }

            else -> {
                val cs = value(it)
                result += cs * temp * ct
                temp = 1
            }
        }
    }
    println(result)
}
