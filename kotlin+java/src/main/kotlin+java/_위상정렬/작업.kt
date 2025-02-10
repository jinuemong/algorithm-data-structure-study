package _위상정렬
// i+1번째 작업을 진행하기 위해서는 list[0]의 시간이 소요
// i+1번째 작업을 진행하기 list[1] 수의 작업을 완료해야 함
// i+1번째 작업을 진행하기 위해서는 list[2...x]의 작업이 이미 종료되어야 한다
// 1번 작업이 5분 걸린다면
// 1번 후에 가능한 2,3번 작업은
// 1번 작업이 종료된 후 실행되어야 한다
// 선행 작업이 있는경우 자신의 weight에 선행 작업의 weight를 더해야 함
fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val graph = Array(n+1){
        mutableListOf<Int>()
    }
    // 각 작업 수행 시간
    val time = Array(n+1){0L}
    // 각 작업 수행 가중치
    val weight = Array(n+1){0L }
    // 서로 선행 관계가 없는 작업들은 동시에 수행이 가능 ->
    val inDegree = Array(n+1){ 0 }
    val que = ArrayDeque<Int>()

    repeat(n){
        val idx = it+1
        val current = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
        time[idx] = current[0].toLong()
        inDegree[idx] = current[1]
        if (current[1] == 0) {
            que.add(idx)
            weight[idx] = time[idx]
        }
        for (i in 2..current.lastIndex){
            graph[current[i]].add(idx)
        }
    }
    while (que.isNotEmpty()){
        val current = que.removeFirst()
        for (next in graph[current]){
            inDegree[next]-=1
            weight[next] = maxOf(weight[next],weight[current]+ time[next])
            if (inDegree[next]==0){
                que.add(next)
            }
        }
    }
    println(weight.max())
}

