package _구현
fun main(){
    val (n,m) = readlnOrNull()
        ?.split(" ")
        ?.map{it.toLong()}
        ?.sorted()
        ?: return

    fun gcd(a: Long, b: Long) : Long {
        var x = a
        var y = b
        while (y != 0L){
            val temp = x % y
            x = y
            y = temp
        }
        return x
    }
    println("1".repeat(gcd(m,n).toInt()))
}
