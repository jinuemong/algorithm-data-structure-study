n, r, c = map(int, input().split())

def find(row,col,n,value):
    n = n //2

    if row < n and col < n:
        if n == 1:
            print(value)
        else:
            find(row,col,n,value)
    elif row < n and col >= n :
        if n == 1:
            print(value + 1)
        else:
            find(row,col - n, n , value + n ** 2 )
    elif row >= n and col < n :
        if n == 1:
            print(value + 2)
        else:
            find(row - n, col, n , value + n ** 2 * 2)
    elif row >=n and col >=n :
        if n == 1:
            print(value + 3 )
        else:
            find(row - n, col - n ,n, value + n ** 2 * 3)
find(r,c,2**n,0)