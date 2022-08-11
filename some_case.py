def same_case(a, b): 
    y=bool(b.isupper())
    x=bool(a.isupper())

 
    if(bool(a.isalpha())and bool(b.isalpha())):
        if(x==y):
            return 1
        elif(a!=b ):
            return 0
    return -1
print(same_case('1', '/'))
