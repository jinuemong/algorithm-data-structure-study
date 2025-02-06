package _위상정렬

fun main(){
    val (n,m) = readlnOrNull()?.split(" ")?.map{it.toInt()}?: return
    val inDegree = Array(n+1){0}
    val graph = List(n+1){
        mutableListOf<Int>()
    }
    val queue = ArrayDeque<Int>()
    val result = mutableListOf<Int>()
    List(m){
        val current = readlnOrNull()?.split(" ")?.map{it.toInt()}?: return
        for (i in 1.. current.lastIndex-1){
            val x = current[i]
            val y = current[i+1]
            inDegree[y]+=1
            graph[x].add(y)
        }
    }

    for (i in 1..inDegree.lastIndex){
        if (inDegree[i]==0){
            queue.add(i)
        }
    }

    while (queue.isNotEmpty()){
        val idx = queue.removeFirst()
        result.add(idx)
        for (current in graph[idx]){
            inDegree[current]-=1
            if (inDegree[current]==0){
                queue.add(current)
            }
        }
    }
    if (result.size==n){
        result.forEach { println(it)}
    } else {
        println(0)
    }
}

// 진입        차수
// 1 -     /  0
// 2 - 6   /  0
// 3 - 4,2 /  0
// 4 - 1,5 /  0
// 5 - 2   /  0
// 6 -     /  0

// 방향
// 1 - 4
// 2 - 5, 3
// 3
// 4 - 3
// 5 - 4
// 6 - 2

// 진입차수가 0인 수를 큐에 추가
// 추가된 큐의 앞부분을 제거하고 방향 그래프를 추가
// 큐에 새로 추가된 정점은 진입 차수가 하나 감소
// 반면 진입 차수가 0인 값은 큐에 추가하지 않음
// 모든 정점을 탐색이 불가능한 경우는 사이클이 존재
// 1 6 4 2 3 5 4
// que = [1,6]
// [6,4]
// [4,2]
// [2,3]
// [3,3,5]
// [3,5]
// [5]
// [4]
// [] -> 3을 넣어야 하지만, 3의 진입차수가 0이므로 제거
