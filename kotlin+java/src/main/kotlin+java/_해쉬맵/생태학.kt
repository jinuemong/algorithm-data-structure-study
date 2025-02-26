package _해쉬맵

import java.util.*

fun main() {
    val three = TreeMap<String, Double>()
    var max = 0.0

    while(true){
        val tmp = readLine() ?: break
        three[tmp] = three.getOrDefault(tmp, 0.0) + 1.0
        max++
    }

    while(three.isNotEmpty()){
        val tmp = three.pollFirstEntry()
        val value = (tmp.value / max)*100
        println("${tmp.key} ${String.format("%.4f", value)}")
    }
}
