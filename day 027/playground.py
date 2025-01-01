
def add(*args):
    x = 0
    for n in args:
        x = n+x
        
    return x


print(add(1,2,3,4))