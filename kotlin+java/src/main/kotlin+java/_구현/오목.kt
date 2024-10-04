package _구현

fun main() {
    val omok = List(19) {
        readlnOrNull()?.split(" ")?.map { it.toInt() } ?: return
    }

    fun dfs(
        current : Int,
        i:Int,
        j:Int,
        dict:Pair<Int,Int>
    ): Boolean{
        var (i,j) = listOf(i,j)
        var count = 1
        while(true){
            i+=dict.first
            j+=dict.second
            if (i !in 0..<19 || j !in 0..<19 || omok[i][j]!=current)
                break
            count++
            if (count > 5) return false
        }
        return count==5
    }
    fun findWinner(
        current: Int,
        i:Int,
        j:Int,
    ): Boolean {
        return dfs(current,i,j,Pair(1,0)) ||
                dfs(current,i,j,Pair(1,1)) ||
                dfs(current,i,j,Pair(0,1)) ||
                dfs(current,i,j,Pair(-1,1))
    }

    for (i in 0..<omok.size) {
        for (j in 0..<omok[0].size) {
            if (omok[i][j] == 1){
                if(findWinner(1,i,j)){
                    return println("${1}\n${i+1} ${j+1}")
                }
            }else if (omok[i][j]==2){
                if (findWinner(2,i,j)){
                    return println("${2}\n${i+1} ${j+1}")
                }
            }
        }
    }
    println(0)
}
