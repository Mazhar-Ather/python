# this program use factorial
# Recursion
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))

# fabonacci series

def fab(n):
    if ( n==0 ) :
        return 0
    elif (n==1):
        return 1
        


    else:
    
        return fab(n-1)+fab(n-2)

print(fab(0))
print(fab(1))
print(fab(2))
print(fab(3))

