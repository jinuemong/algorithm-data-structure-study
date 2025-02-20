package _재귀

fun hanoi(n: Int, from: Int, to: Int, via: Int, sb: StringBuilder) {
    if (n == 1) {
        sb.append("$from $to\n")
        return
    }
    hanoi(n - 1, from, via, to, sb)
    sb.append("$from $to\n")
    hanoi(n - 1, via, to, from, sb)
}

fun main() {
    val n = readlnOrNull()?.toInt() ?: return

    val sb = StringBuilder()
    hanoi(n, 1, 3, 2, sb)

    println((1 shl n) - 1)
    print(sb.toString())
}

// 1 3 2 1
// 2
// 3

// 1 3 2 1
// 2
// 3 1

// 1 3
// 2 2
// 3 1

// 1 3
// 2 2 1
// 3

// 1
// 2 2 1
// 3 3

// 1 1
// 2 2
// 3 3

// 1 1
// 2
// 3 3 2

// 1
// 2
// 3 3 2 1
