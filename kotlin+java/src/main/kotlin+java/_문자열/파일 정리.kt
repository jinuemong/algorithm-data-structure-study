package _문자열

fun main(){
    val result = mutableMapOf<String,Int>()
    repeat(readlnOrNull()?.toInt() ?:return){
        val input = readlnOrNull()?: return
        val index = input.indexOf(".")
        val current = input.slice(index+1 until input.length)
        if (current in result){
            result[current] = result[current]?.plus(1) ?: return
        }else{
            result[current] = 1
        }
    }
    result.keys.toList().sorted().forEach {
        println("$it ${result[it]}")
    }
}
