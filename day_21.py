# def name(a="Muhammad",b="Mazhar",c="Ather"):
#     print("Hello",a,b,c)

# name()

# def name_by_user():
#     a=input("Enter first name: ")
#     b=input("Enter middle name: ")
#     c=input("Enter last name: ")
#     print("hello",a.title(),b.capitalize(),c.upper())

# name_by_user()

# def avg(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("average of numbers", sum/len(numbers))    

# avg(2,3,4,3,4,2)

def names(**name):
    numbers=[]
    for i in range (0,4):
        i=int(input("Enter numbers: "))
        numbers.append(i)
    for y in name.values():
        numbers.append(y)
    hi=sum(numbers)
    print("average of numbers ",hi/len(numbers))

names()

# def names(**name):
#     numbers = []
#     for i in range(4):
#         num = int(input("Enter a number: "))
#         numbers.append(num)
        
#     for y in name.values():
#         numbers.append(y)
    
#     total_sum = sum(numbers)
#     print("Average of numbers:", total_sum / len(numbers))

# names()