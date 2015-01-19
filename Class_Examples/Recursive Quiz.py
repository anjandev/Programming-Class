numcalls = 0

def seq_tri(n):
    global numcalls
    numcalls += 1
    if n == 1:
        return 1
    else:
        return seq_tri(n - 1) + n
   
    
print seq_tri(8)

print numcalls


numcalls = 0

def seq_sq(n):
    global numcalls
    numcalls += 1
    
    if n == 1:
        return 2
    else:
        return seq_sq(n - 1) + n * 2
   
    
print seq_sq(10)

print numcalls
