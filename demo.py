from tkinter import *

root = Tk()
# root.geometry('219x253')#修改窗口大小
root.title('计算器')#窗口标题
# 设置窗口大小与初始位置，大小为219x253,位置为(800,300)
root.geometry("219x253+800+300")
root.resizable(width=False, height=False) # 设置窗口大小不可改变

text = Entry(root, font=("Calibri", 15))
text.place(x=5, y=5, width=209, height=40)


def main():
    running = 1
    Button(root, text="1", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : add(1))\
        .place(x=5, y=55, width=50, height=45)
    Button(root, text="2", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : add(2)) \
        .place(x=58, y=55, width=50, height=45)
    Button(root, text="3", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : add(3)) \
        .place(x=111, y=55, width=50, height=45)
    Button(root, text="4", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : add(4)) \
        .place(x=5, y=105, width=50, height=45)
    Button(root, text="5", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : add(5)) \
        .place(x=58, y=105, width=50, height=45)
    Button(root, text="6", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : add(6)) \
        .place(x=111, y=105, width=50, height=45)
    Button(root, text="7", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : add(7)) \
        .place(x=5, y=155, width=50, height=45)
    Button(root, text="8", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : add(8)) \
        .place(x=58, y=155, width=50, height=45)
    Button(root, text="9", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : add(9)) \
        .place(x=111, y=155, width=50, height=45)
    Button(root, text="0", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : add(0)) \
        .place(x=58, y=205, width=50, height=45)
    Button(root, text="+", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : po('+')) \
        .place(x=164, y=55, width=50, height=45)
    Button(root, text="-", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : po('-')) \
        .place(x=164, y=105, width=50, height=45)
    Button(root, text="*", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : po('*')) \
        .place(x=164, y=155, width=50, height=45)
    Button(root, text="/", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : po('/')) \
        .place(x=164, y=205, width=50, height=45)
    Button(root, text="=", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=lambda : re('=')) \
        .place(x=111, y=205, width=50, height=45)
    Button(root, text="AC", width=10, bg='#FFC0CB',activebackground='#A9A9A9', command=ac) \
        .place(x=5, y=205, width=50, height=45)
    # Button(root, text = "退出", width = 10, command = root.quit)\
    #     .place(x=230,y=230,width = 80,height=40)
    if running == 1:
        root.mainloop()

class S():
    def __init__(self):
        self.mul1 = 0
        self.mul2 = 0
        self.q = '+'
        self.flag = 0

def add(c):
    if c >= 0 and c <= 9:
        text.insert(len(text.get()), c)

def re(c):
    if s.flag == 1:
        s.mul2 = int(text.get())

        if s.mul2 == 0:
            s.mul1 += s.mul2
        if s.q == '+':
            s.mul1 += s.mul2
        elif s.q == '-':
            s.mul1 = s.mul1 - s.mul2
        elif s.q == '*':
            s.mul1 = s.mul1 * s.mul2
        elif s.q == '/':
            s.mul1 = s.mul1 / s.mul2
        text.delete(0, len(text.get()))
        text.insert(len(text.get()), s.mul1)
    else:
        s.mul1 = int(text.get())
        text.delete(0, len(text.get()))
        text.insert(len(text.get()), s.mul1)

def po(c):
    s.q = c
    if s.flag == 0:
        s.mul1 = int(text.get())
    else:
        try:
            s.mul2 = int(text.get())
        except:
            s.mul2 = float(text.get())
    text.delete(0, len(text.get()))
    s.flag = 1

    # if c == '+':
    #     mul1 = mul1 + mul2
    # elif c== '-':
    #     mul1 = mul1 - mul2
    # elif c== '*':
    #     mul1 = mul1 * mul2
    # elif c == '/':
    #     mul1 = mul1 / mul2



def ac():
    s.flag = 0
    s.mul1 = 0
    s.mul2 = 0
    s.q = '+'
    text.delete(0, len(text.get()))

if __name__ == '__main__':
    s = S()
    main()
