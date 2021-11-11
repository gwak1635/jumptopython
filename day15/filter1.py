def positive(x):
    if x>0:
        return x

print(list(filter(positive, [1,2,3,4,-1,-3])))

def negative(x):
    if x<0:
        return x

print(filter(negative, -3))