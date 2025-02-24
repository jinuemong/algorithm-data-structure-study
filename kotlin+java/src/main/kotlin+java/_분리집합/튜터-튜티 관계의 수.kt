package _분리집합

fun main(){
    val (n,m) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val parent = Array(n+1){it}

    fun find(x: Int): Int{
        if (parent[x] != x){
             parent[x] = find(parent[x])
        }
        return parent[x]
    }

    fun union(x:Int,y:Int){
        val px = find(x)
        val py = find(y)

        if (px!=py){
            parent[px] = py
        }
    }

    repeat(m){
        val (x,y) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
        union(x,y)
    }
    val result = IntArray(n+1)
    for(i in 1..n){
        result[find(i)]++
    }
    var count = 1L
    result.forEach{
        if(it!=0) count = (count*it)%1_000_000_007
    }
    println(count%1_000_000_007)
}
