package _최소신장트리

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private data class Planet(
    val x : Int,
    val y : Int,
    val z : Int,
    val i : Int
)

fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    var stk : StringTokenizer
    val n = br.readLine().toInt()
    val parent = IntArray(n){ i -> i }

    fun findParent(x: Int): Int{
        if(x == parent[x]) return x
        parent[x] = findParent(parent[x])
        return parent[x]
    }

    fun union(a : Int, b: Int) {
        val A = findParent(a)
        val B = findParent(b)
        if (A == B) return
        parent[B] = A
    }
    val starArray = Array(n){ Planet(0, 0, 0, 0) }
    val edgeList : MutableList<Triple<Int, Int, Int>> = mutableListOf()
    repeat(n){ i ->
        stk = StringTokenizer(br.readLine ())
        val x = stk.nextToken().toInt()
        val y = stk.nextToken().toInt()
        val z = stk.nextToken().toInt()
        starArray[i] = Planet(x, y, z, i)
    }
    val xList = starArray.sortedWith(compareBy{ it.x })
    val yList = starArray.sortedWith(compareBy{ it.y })
    val zList = starArray.sortedWith(compareBy{ it.z })
    for(i in 0 until n - 1){
        edgeList.add(Triple(xList[i].i, xList[i + 1].i , xList[i + 1].x - xList[i].x))
        edgeList.add(Triple(yList[i].i, yList[i + 1].i, yList[i + 1].y - yList[i].y))
        edgeList.add(Triple(zList[i].i, zList[i + 1].i, zList[i + 1].z - zList[i].z))
    }
    edgeList.sortWith( compareBy{ it.third } )
    var totalCost = 0
    edgeList.forEach{
        val a = it.first
        val b = it.second
        val cost = it.third
        if(findParent(a) != findParent(b)){
            union(a, b)
            totalCost += cost
        }
    }
    print(totalCost)
}
