package _이분탐색
fun main() {
    val n = readlnOrNull()?.toInt() ?: return
    val nList = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    val lis = IntArray(n)

    fun binarySearchIndex(start:Int,end:Int, target: Int): Int{
        var start = start
        var end = end
        var mid : Int
        while (start < end){
            mid = (start+end)/2
            if (lis[mid]<target){
                start = mid+1
            }else{
                end = mid
            }
        }
        return end
    }

    var j = 0
    var i = 1
    lis[0] = nList[0]
    while(i < n){
        if (lis[j]<nList[i]){
            lis[j+1] = nList[i]
            j+=1
        }else{
            val idx = binarySearchIndex(0,j,nList[i])
            lis[idx] = nList[i]
        }
        i+=1
    }
    println(j+1)


}

