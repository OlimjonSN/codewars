def warn_the_sheep(q):
    
    if len(q)-1-q.index('wolf')==0:
        return "Pls go away and stop eating my sheep"    
    return "Oi! Sheep number {}! You are about to be eaten by wolves!".format(len(q)-q.index('wolf') )
print(warn_the_sheep(["sheep","wolf"]))
