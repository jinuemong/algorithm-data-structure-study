package _문자열

fun main() {
    // R : 뒤집기 -> 배열의 순서 뒤집기
    // D : 버리기 -> 첫 번째 수를 버리기
    // RDD : 뒤집기, 버리기, 버리기
    repeat(readlnOrNull()?.toInt() ?: return) {
        val ac = readlnOrNull() ?: return
        val p = readlnOrNull()?.toInt() ?: return
        val input = readlnOrNull()?.filter { it !in "[]" } ?: return
        val list = if (input == "") emptyList()
        else input.filter { it !in "[]" }.split(",").map { it.toInt() }

        fun ac(): String {
            var isReverse = false
            val deque = ArrayDeque<Int>()
            deque.addAll(list)
            ac.forEach {
                if (it == 'R'){
                    isReverse = !isReverse
                }else {
                    if (deque.isEmpty()) return@ac "error"
                    if (isReverse){
                        deque.removeLast()
                    }else {
                        deque.removeFirst()
                    }
                }
            }
            if (isReverse) deque.reverse()
            return "[${deque.joinToString(",")}]"
        }
        println(ac())
    }
}

// RDD
// 뒤집기 연산은 나중에 수행해도 된다
// 안 뒤집어진 상태인 경우 -> D는 첫번째에서 삭제
// 뒤집어진 상태인 경우 -> D는 마지막에서 삭제
// deque로 만든 후 현재 방향을 지정해서 삭제한다
// 삭제를 수행할 수 없는 경우 error 출력


