package _구현

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))

    val n = reader.readLine().toInt()
    val p = IntArray(n)
    val order = IntArray(n)
    val cards = IntArray(n)

    val st = StringTokenizer(reader.readLine())
    for (i in 0 until n) {
        p[i] = st.nextToken().toInt()
    }

    val st2 = StringTokenizer(reader.readLine())
    for (i in 0 until n) {
        order[st2.nextToken().toInt()] = i
        cards[i] = i % 3
    }

    val compare = cards.clone()
    val next = IntArray(n)

    var result = 0
    while (!cards.contentEquals(p) && !(result != 0 && cards.contentEquals(compare))) {
        for (j in 0 until n) {
            next[order[j]] = cards[j]
        }

        System.arraycopy(next, 0, cards, 0, n)
        result++
    }

    if (result != 0 && cards.contentEquals(compare)) {
        println(-1)
    } else {
        println(result)
    }
}

// 0 1 2 idx
// 0 1 2 card
// 1 2 0 first
// 2 0 1 nex
// 2 0 1
