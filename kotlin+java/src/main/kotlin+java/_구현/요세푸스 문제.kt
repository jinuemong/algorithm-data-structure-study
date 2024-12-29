package _구현

fun main() {
    val (n, k) = readlnOrNull()
        ?.split(" ")
        ?.map { it.toInt() } ?: return
    val result = mutableListOf<Int>()
    val data = ArrayDeque<Int>()
    data.addAll(1..n)
    var count = 0
    while (data.isNotEmpty()){
        count+=1
        if (count == k){
            count = 0
            result.add(data.removeFirst())
        } else {
            data.addLast(data.removeFirst())
        }
    }
    println("<"+result.joinToString(", ")+">")
}

// 1 2 3 4 5 6 7

// 3

// 1 2 x 4 5 6 7

// 1 2 x 4 5 x 7

