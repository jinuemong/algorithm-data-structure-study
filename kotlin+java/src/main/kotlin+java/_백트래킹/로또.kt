package _백트래킹
fun main(){
    fun makeS(s:List<String>):Pair<Int,List<Int>>{
        return s[0].toInt() to s.subList(1,s.size).map{it.toInt()}
    }
    while(true){
        val s = readlnOrNull()?.run {
            if(this=="0") 0 to listOf()
            else makeS(this.split(" "))
        }?: return
        if (s.second.isEmpty()) break

        fun backTracking(start:Int,current:MutableList<Int> ,visited: BooleanArray){
            if(current.size == 6){
                println(current.joinToString(" "))
            }else{
                for(i in start..<s.first){
                    if (visited[i]) continue
                    visited[i] = true
                    backTracking(i,(current+s.second[i]).toMutableList(),visited)
                    visited[i] = false
                }
            }
        }
        backTracking(0,mutableListOf(),BooleanArray(s.first){false})
        println()
    }
}
