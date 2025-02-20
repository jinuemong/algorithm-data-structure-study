package _구현// recommend 1 => 가장 어려운 & 큰 문제 번호
// recommend 2 => 가장 쉬운 & 작은 문제 번호
// add P L => 난이도가 L, 문제 번호 P 추가
// - 같은 번호로는 안들어옴(동시에) 다시 들어올 순 있음
// solved P => 번호 P 제거
// - 있는 번호만 주어짐
import java.util.PriorityQueue

fun main() {
    val n = readlnOrNull()?.toInt() ?: return

    val trash = mutableMapOf<Int, MutableSet<Int>>()

    val upQue = PriorityQueue<Pair<Int, Int>>(compareBy({ -it.second }, { -it.first }))
    val downQue = PriorityQueue<Pair<Int, Int>>(compareBy({ it.second }, { it.first }))

    repeat(n) {
        val (p, l) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
        upQue.add(p to l)
        downQue.add(p to l)
    }

    val m = readlnOrNull()?.toInt() ?: return
    repeat(m) {
        val c = readlnOrNull()?.split(" ") ?: return
        when (c[0]) {
            "add" -> {
                val p = c[1].toInt()
                val l = c[2].toInt()
                trash[p]?.remove(l)
                upQue.add(p to l)
                downQue.add(p to l)
            }

            "solved" -> {
                val p = c[1].toInt()
                val (_, l) = upQue.find { it.first == p } ?: return@repeat
                trash.computeIfAbsent(p) { mutableSetOf() }.add(l)
            }

            "recommend" -> {
                val x = c[1].toInt()
                if (x == 1) {
                    while (trash[upQue.peek().first]?.contains(upQue.peek().second) == true) {
                        upQue.poll()
                    }
                    println(upQue.peek().first)
                } else {
                    while (trash[downQue.peek().first]?.contains(downQue.peek().second) == true) {
                        downQue.poll()
                    }
                    println(downQue.peek().first)
                }
            }
        }
    }
}
//// 연결리스트 방식 실패
//private data class Node21939(
//    val p: Int, // 문제 번호
//    val l: Int, // 난이도
//)
//
//private data class Graph21939(
//    var value: Node21939? = null,
//    var prev: Graph21939? = null,
//    var next: Graph21939? = null,
//)
//
//fun main() {
//    val n = readlnOrNull()?.toInt() ?: return
//    val root = Graph21939()
//    var head = 0
//    var tail = 0
//
//    // 문제 추가
//    fun add(newNode: Node21939) {
//        // 첫 추가
//        if (root.value == null) {
//            root.value = newNode
//            head = newNode.p
//            tail = newNode.p
//            return
//        }
//
//        var current: Graph21939 = root
//        while (
//            current.next != null &&
//            (current.next!!.value!!.l < newNode.l ||
//                    (current.next!!.value!!.l == newNode.l && current.next!!.value!!.p < newNode.p))
//        ) {
//            current = current.next!!
//        }
//        val temp = current.next
//        val new = Graph21939(
//            prev = current,
//            value = newNode,
//            next = temp
//        )
//        current.next = new
//        temp?.prev = new
//        if (new.prev == null) {
//            head = new.value!!.p
//        } else if (new.next == null) {
//            tail = new.value!!.p
//        }
//    }
//
//    // 문제 삭제
//    fun delete(target: Int) {
//        var current: Graph21939? = root
//
//        while (current != null) {
//            if (current?.value?.p == target) break
//            current = current?.next
//        }
//        current?.prev?.next = current?.next
//        current?.next?.prev = current?.prev
//
//        if (current?.prev == null) {
//            head = current?.next?.value!!.p
//        } else if (current?.next == null) {
//            tail = current?.prev?.value!!.p
//        }
//    }
//
//    // 첫 번째 줄에 주어진 문제들 추가
//    List(n) {
//        val (p, l) = readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
//        add(Node21939(p = p, l = l))
//    }
//
//    // 두 번째 줄에 명령어의 개수
//    val m = readlnOrNull()?.toInt() ?: return
//    List(m) {
//        val c = readlnOrNull()?.split(" ") ?: return
//        when (c[0]) {
//            "add" -> {
//                val (_, p, l) = c
//                val new = Node21939(
//                    p = p.toInt(),
//                    l = l.toInt(),
//                )
//                add(new)
//            }
//
//            "solved" -> {
//                val (_, p) = c
//                delete(p.toInt())
//            }
//
//            "recommend" -> {
//                val (_, x) = c
//                if (x == "1") {
//                    // 가장 어려운 문제 (tail에서 출력)
//                    println(tail)
//                } else {
//                    // 가장 쉬운 문제 (head에서 출력)
//                    println(head)
//                }
//            }
//        }
//    }
//}
//
