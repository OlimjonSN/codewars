def flip(d, a): 
    a.sort()
    if(d=="L"):
        return a.reverse()
        
    return a
print(flip('R', [3, 2, 1, 2]))