# this program use match statement
x=int(input("enter any value: "))
match x:
    case 0:
        print("imran khan")
    case 1:
        print("nawaz shareef")
    # case _:
    #     print("zardari")
    
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)            