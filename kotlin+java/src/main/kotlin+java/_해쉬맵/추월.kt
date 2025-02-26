package _해쉬맵

fun main() {
    val n = readlnOrNull()?.toInt() ?: return

    val carOrder = mutableMapOf<String, Int>()
    repeat(n) { i ->
        val car = readlnOrNull() ?: return
        carOrder[car] = i
    }

    val exitOrder = mutableListOf<String>()
    repeat(n) {
        val car = readlnOrNull() ?: return
        exitOrder.add(car)
    }

    var result = 0
    for (i in 0 until n - 1) {
        for (j in i + 1 until n) {
            if (carOrder[exitOrder[i]]!! > carOrder[exitOrder[j]]!!) {
                result++
                break
            }
        }
    }

    println(result)
}

// 나갈 순서를 저장
//3
//2
//1
//0

// 나갈 순서가 앞서는 경우 앞선 차량
//0
//1 3이어야 하는데 1 ! 앞선
//2
//3
