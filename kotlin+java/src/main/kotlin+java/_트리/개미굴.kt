package _트리

import java.util.TreeMap

private data class Tree14725(
    val value: String,
    val child: TreeMap<String, Tree14725>
)

fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val root = Tree14725("root", TreeMap())

    fun add(list: List<String>) {
        var current = root
        var i = 0
        while (i < list.size) {
            val next = current.child[list[i]]
            if (next == null) {
                val new = Tree14725(list[i], TreeMap())
                current.child[list[i]] = new
                current = new
            } else {
                current = next
            }
            i++
        }
    }
    repeat(n) {
        val list = readlnOrNull()?.split(" ") ?: return
        add(list.subList(1, list.size))
    }
    fun dfs(d: Int, tree: Tree14725){
        println("${"-".repeat(2 * d)}${tree.value}")
        tree.child.forEach {
            dfs(d+1, it.value)
        }
    }
    root.child.forEach {
        dfs(0,it.value)
    }

}
