package _그리디

import java.util.Stack

fun main() {
    val input = readlnOrNull() ?: return
    val stack = Stack<Char>()
    input.forEach {
        if (stack.size == 0){
            stack.add(input[0])
        }else{
            if (stack.lastElement() != it){
                stack.add(it)
            }
        }
    }
    val zeroCount = stack.count{ it == '0' }
    println(minOf(zeroCount,stack.size - zeroCount))
}
