f = open("D:/Onedrive/Coding/Study/Python/day10/새빠일.txt",'r')
while True:
    line=f.readline()
    if not line:break
    print(line)
f.close()