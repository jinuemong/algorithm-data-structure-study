package _구현

import kotlin.math.sqrt

fun main() {
    val n = readlnOrNull()?.toInt()?:return
    val an = BooleanArray(10000001){ true }
    an[0] = false
    an[1] = false

    for (i in 2..sqrt((an.size).toDouble()).toInt()){
        if (an[i]){
            for ( j in i*i..<an.size step i){
                an[j] = false
            }
        }
    }

    fun isPal(data:String): Boolean{
        return (0 until data.length/2).all{
            data[it] == data[data.lastIndex-it]
        }
    }

    for (k in n..10000000){
        if (an[k] && isPal(k.toString())){
            return println(k)
        }
    }
}


// 1000001은 소수 + 팰린드롬


// 1 2 3 4 5 6 7 8 9 10
