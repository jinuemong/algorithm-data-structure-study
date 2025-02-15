package _백트래킹
// 계란으로 계란치면 서로 상대 무게 만큼 내구도가 깍임
// 무게가 0이하가 되면 깨짐
// 가장 왼쪽의 계란을 든다
// 나머지 계란 중 깨지지 않는 다른 계란을 침
// 가장 왼쪽의 계란이 깨졌거나, 깨지지 않는 계란이 없으면 치지 않음
// 가장 최근에 든 계란의 바로 오른쪽 계란을 들고 반복
// 가장 최근에 든 계란이 마지막 계란일 결루 종료

// 1순위 : 현재 든 계란 깨기
// 2순위 : 현재 든 계란으로 가장 많은 계란 깨는 경우 체크
// 매 순간 가장 많이 깨고 넘어가야 함
fun main() {
    val n = readln().toInt()
    val egg = Array(n) {
        val (s, w) = readln().split(" ").map { it.toInt() }
        s to w
    }

    fun dfs(idx: Int, eggs: Array<Pair<Int, Int>>): Int {
        if (idx == n) return eggs.count { it.first <= 0 } // 모든 계란을 다 들었으면 깨진 계란 개수 반환

        if (eggs[idx].first <= 0) return dfs(idx + 1, eggs) // 현재 계란이 깨졌으면 다음 계란으로 넘어감

        var maxBroken = 0
        var hit = false

        for (i in eggs.indices) {
            if (i != idx && eggs[i].first > 0) { // 자기 자신이 아니고 깨지지 않은 계란이면
                hit = true

                // 현재 계란과 상대 계란의 내구도 감소
                eggs[idx] = eggs[idx].first - eggs[i].second to eggs[idx].second
                eggs[i] = eggs[i].first - eggs[idx].second to eggs[i].second

                // 다음 계란을 치러 감
                maxBroken = maxOf(maxBroken, dfs(idx + 1, eggs))

                // 백트래킹 (원래 상태로 복구)
                eggs[idx] = eggs[idx].first + eggs[i].second to eggs[idx].second
                eggs[i] = eggs[i].first + eggs[idx].second to eggs[i].second
            }
        }

        // 만약 칠 수 있는 계란이 없었다면 그냥 다음 계란으로 넘어감
        if (!hit) maxBroken = maxOf(maxBroken, dfs(idx + 1, eggs))

        return maxBroken
    }

    println(dfs(0, egg))
}
