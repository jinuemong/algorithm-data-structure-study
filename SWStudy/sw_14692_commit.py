TC = int(input())
for t in range(1,TC+1):
    N = int(input())
    if N%2==0:
        print("#"+str(t),"Alice")
    else:
        print("#" + str(t), "Bob")