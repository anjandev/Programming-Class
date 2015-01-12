# Recursive Function Examples

# Recursive Factorial Function
# n! = n*(n-1)*(n-2)*.....*2*1

def factorial(n):
    if n == 1:
        print "returning 1"
        return 1
    else:
        result = n*factorial(n-1)
        print "returning", result
        return result
    
print factorial(5)


# Fibonacci Sequence: 1,1,2,3,5,8,13,21,......
# t[n]= t[n-2]+t[n-1]

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)
    
print fib(4)
