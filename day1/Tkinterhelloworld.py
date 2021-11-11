#thinter로 hello world 출력하기
#utf-8 

from tkinter import *

#Tk클래스의 a객체 생성같은건가?
win= Tk()#화면 생성!
win.title("Echo's 1st GUI")#화면의 타이틀
win.geometry("300x200+100+100")
win.resizable(False,False)

lab=Label(win, text='Hello World',width=10, height=2, fg='blue', relief='solid')#레이블 생성!
#width=커다란 글자 개수, height=줄 개수 fg=폰트색상, relief=테두리
lab.pack()

top = Tk()

B1 = Button(top, text ="FLAT", relief=FLAT )
B2 = Button(top, text ="RAISED", relief=RAISED )
B3 = Button(top, text ="SUNKEN", relief=SUNKEN )
B4 = Button(top, text ="GROOVE", relief=GROOVE )
B5 = Button(top, text ="RIDGE", relief=RIDGE )
B6 = Button(top, text ="SOLID", relief=SOLID )
B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
B6.pack()

top.mainloop()#모든 창을 닫기 전까지 이 명령어 뒤로 넘어가지 않음.