package _소수
fun main() {
    val (a,b) = readlnOrNull()?.split(" ")?.map{it.toInt()} ?: return
    // a~b 사이의 언더프라임 개수
    // 언더프라임은 구성하는 소수 목록의 길이가 소수인 것
    // 소인수 분해 방법 ! 작은 소수부터 나눠보기
    val so = BooleanArray(maxOf(a,b)+1){true}
    so[0] = false
    so[1] = false
    for (i in 2..<so.size){
        if (so[i]){
            for (j in 2*i..<so.size step i){
                so[j] = false
            }
        }
    }

    fun under(value: Int): Boolean{
        var i = 2
        var result = 0
        var current = value
        while(current>1){
            if(so[i]&&current%i==0){
                current/=i
                result+=1
            }else {
                i++
            }
        }
        return so[result]
    }
    var result = 0
    for(i in a..b){
        if(under(i)) result++
    }
    println(result)
}
