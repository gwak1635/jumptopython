
def gugu(n):
    list=[]
    for i in range(1,10):
        list.append(n*i)
    return list



a=int(input("구구단 프로그램\n정수 입력:"))

result = gugu(a)
print(result)