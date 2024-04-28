def prod(n1,n2):
    
    
    if n2 == 1:
        return n1
    
    
    else:
        return n1 + prod(n1,n2-1)
    
    # return n1 * n2
    
    
print(prod(1,5))