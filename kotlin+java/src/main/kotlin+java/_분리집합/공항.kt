package _분리집합
// 부모를 따라 이동하며, 다음 값이 이미 찼으면 못 넣고 종료
fun main(){
    val g = readlnOrNull()?.toInt() ?: return
    val p = readlnOrNull()?.toInt() ?: return
    val parent = IntArray(g+1){it}

    fun find(x: Int): Int {
        if (parent[x] == x) return x
        parent[x] = find(parent[x])
        return parent[x]
    }

    fun union(a: Int, b: Int){
        parent[a] =  b
    }

    var count = 0
    repeat(p){
        val gi = readlnOrNull()?.toInt() ?: return
        val dockingGate = find(gi)
        if (dockingGate == 0) return println(count)

        union(dockingGate, dockingGate - 1)
        count++
    }
    println(count)
}
