fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val ex = readlnOrNull()
        ?.split(" ") ?: return
    var visited = BooleanArray(10)
    val ans = mutableListOf<String>()

    fun dfs(start: Int, depth: Int, word: String) {
        if(depth == n) {  // 부등호 개수만큼 숫자를 배치했으면
            ans.add(word)  // 그 숫자 조합을 답안 리스트에 추가
            return
        }
        for(i in 0 until 10) {  // 0부터 9까지 가능한 숫자들에 대해
            if(visited[i]) continue  // 이미 사용된 숫자는 넘긴다
            if(ex[depth] == ">") {  // 부등호가 ">"이면
                if(start > i) {  // start 숫자가 i보다 크면
                    visited[i] = true  // 해당 숫자 사용 표시
                    dfs(i, depth + 1, word + i)  // 다음 깊이로 진행
                    visited[i] = false  // 탐색 끝난 후 복구
                }
            } else {  // 부등호가 "<"이면
                if(start < i) {  // start 숫자가 i보다 작으면
                    visited[i] = true  // 해당 숫자 사용 표시
                    dfs(i, depth + 1, word + i)  // 다음 깊이로 진행
                    visited[i] = false  // 탐색 끝난 후 복구
                }
            }
        }
    }

    for(i in 0 until 10) {
        visited = BooleanArray(10)
        visited[i] = true
        dfs(i, 0, "$i")
        visited[i] = false
    }

    println(ans.last())
    println(ans.first())
}

// 양방향 큐 활용
// 2개 주어지면 -> 3자리수
// 9개 주어지면 -> 10자리수
// 가장 큰 수의 자리수를찾고 좌우로 스택 ?

// 897
// 021

//897
//021
