package _문자열

import java.util.Stack

fun main() = with(System.`in`.bufferedReader()){
    repeat(readLine().toInt()){
        val stack = Stack<Char>()
        var flag = "YES"
        readLine().forEach {
            if (it == '('){
                stack.add(it)
            }else{
                if(stack.size > 0){
                    stack.pop()
                }else{
                    flag = "NO"
                    return@forEach
                }
            }
        }
        if (stack.size > 0 ) flag = "NO"
        println(flag)
    }
}
