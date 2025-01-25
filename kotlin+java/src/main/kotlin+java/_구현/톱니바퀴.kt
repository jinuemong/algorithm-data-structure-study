package _구현
import kotlin.math.pow
fun main(){
    // n : 0, s : 1
    // 상태는 12시 방향 부터 주어진다.
    // 즉 <-3번째 값(인덱스 2), ->7번째 값(인덱스 6)가 맞닿는 부분이다.
    // 맞닿는 극이 달라야 회전 한다 -> 두 극을 곱하여 0이면 노회전, 1이면 회전
    // 시계 방향 회전 : 뒤 -> 앞
    // 시계 반대 방향 회전 : 앞 -> 뒤
    val states = List(4) {
        val state = readlnOrNull()?.map { it.digitToInt() } ?: return
        ArrayDeque(state)
    }
    val k = readlnOrNull()?.toInt() ?: return
    val rotations = List(k) {
        readlnOrNull()?.split(" ")?.map { it.toInt() }?.toIntArray() ?: return
    }

    fun setState(d: Int, state: ArrayDeque<Int>) {
        if (d == 1) { // 시계 방향
            state.addFirst(state.removeLast())
        } else { // 반시계 방향
            state.addLast(state.removeFirst())
        }
    }

    fun calculateRotation(idx: Int, direction: Int): IntArray {
        val directions = IntArray(4) { 0 }
        directions[idx] = direction

        // 왼쪽 톱니바퀴 회전 방향 계산
        for (i in idx downTo 1) {
            if (states[i][6] != states[i - 1][2]) {
                directions[i - 1] = -directions[i]
            } else {
                break
            }
        }

        // 오른쪽 톱니바퀴 회전 방향 계산
        for (i in idx until 3) {
            if (states[i][2] != states[i + 1][6]) {
                directions[i + 1] = -directions[i]
            } else {
                break
            }
        }

        return directions
    }

    rotations.forEach { (num, d) ->
        val directions = calculateRotation(num - 1, d)
        directions.forEachIndexed { index, direction ->
            if (direction != 0) setState(direction, states[index])
        }
    }

    val result = states.mapIndexed { index, it ->
        if (it[0] == 1) 2.0.pow(index).toInt() else 0
    }.sum()

    println(result)
}
