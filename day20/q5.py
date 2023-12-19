

def pibonachi (n):
    arr=[0,1]
    b=0
    index=1
    while True:
        b=arr[index-1]+arr[index]
        if b>n:
            break
        index+=1
        arr.append(b)
    return arr

print(pibonachi(1000))