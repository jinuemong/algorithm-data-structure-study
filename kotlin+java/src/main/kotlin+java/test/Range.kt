package test

fun showRange(r: IntProgression){
    for (i in r){
        println(i)
    }
}

fun main(){
    val data = readlnOrNull()?.toInt() ?: return

    showRange(0..data)
}

