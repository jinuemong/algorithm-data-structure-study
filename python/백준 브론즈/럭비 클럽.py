while True:
    name,age,w = input().split()
    age ,w  = int(age), int(w)
    if name == "#" and age == 0 and w == 0:
        break
    if age >17 or w >=80:
        print(name,"Senior")
    else:
        print(name,"Junior")
