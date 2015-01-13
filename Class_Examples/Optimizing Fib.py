# Practice optimizing recursive functions using dictionaries

fibnumbers = {}

basecasetime = 0
old_basecasetime = 0

def fib(n):
    # New fib function using dictionaries
    global fibnumbers, basecasetime
    
    if n == 1 or n == 2:
        basecasetime = basecasetime + 1
        return 1
    elif n not in fibnumbers:
        finnum = fib(n-2) + fib(n-1)
        fibnumbers[n] = finnum
        return finnum
    else:
        return fibnumbers[n]
    
def oldfib(n):
    # Old fib function not using dictionaries
    global old_basecasetime
    
    if n == 1 or n == 2:
        old_basecasetime = old_basecasetime + 1
        return 1
    else:        
        return oldfib(n-2) + oldfib(n-1)

    
print fib(7)
print basecasetime


print oldfib(7)
print old_basecasetime
