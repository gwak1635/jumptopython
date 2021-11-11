f = open("D:/Onedrive/Coding/Study/Python/day10/새빠일.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()