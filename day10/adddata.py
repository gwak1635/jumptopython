f = open("D:/Onedrive/Coding/Study/Python/day10/새빠일.txt",'a')
for i in range(11,20):
    data= "%d번째 줄입니다." % i
    f.write(data)
f.close()