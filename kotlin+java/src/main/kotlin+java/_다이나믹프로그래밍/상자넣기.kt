package _다이나믹프로그래밍

fun main(){
    val n =readlnOrNull()?.toInt() ?: return
    val nm = readlnOrNull()?.split(" ")?.map{it.toInt()}?:return
    val result = IntArray(n){ 1 }

    for (i in 1..<n){
        for (j in 0..<i){
            if (nm[j]<nm[i]) {
                result[i] = maxOf(result[i], result[j] + 1)
            }
        }
    }
    println(result.max())
}

//idx 0 1 2 3 4
//val 1 5 2 3 7 - nm
//res 1 1 1 1 1

// i = 1 nm[i] = 1
// j = 0  j = 1 nm[j](0) -> 1, nm[j](1) -> 5
// 더 크다면 선택이 가능하다.
// i = 2 nm[i] = 2
// j = 0,1,2 -> nm(j) 1,5,2
// 이전까지 선택한 것들보다 크다면 새로 선택, 갱신
// 즉 i번째 값을 선택할 때 i-1번째 값들 중에 다음에 선택이 가능하다면 i번째 값 선택
// dp[i]는 i번째까지 선택한 수
