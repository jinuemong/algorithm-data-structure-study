package _그리디
// 지나간 부분은 다시 돌아오지 않으므로, 앞에서부터 최대한 많은 부분을 가져가자
// 2> 3개
// 1 2 3 4 5 6
// [ ] [ ] [ ]
// 3> 2개
// 1 2 3 4 5 6
// [   ] [   ]
// 4> 2개
//


 fun main() {
     val (n,l) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
     val location = readlnOrNull()?.split(" ")?.map{it.toInt()}?.sorted() ?: return
     var count = 1
     if (location.size == 1) return println(count)
     var current = location[0]+l-1

     for (i in 1..location.lastIndex){
         if (location[i]>current){
             current = location[i]+l-1
             count++
         }
     }
     println(count)
 }
