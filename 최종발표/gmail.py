from tkinter import*
from tkinter import ttk

class main:
    def __init__(self, message): # message: 메일에 보내질 내용
        self.window = Tk()
        self.window.title("Gmail")
        self.window.geometry("400x200")

        self.message = message

        sEmail = Label(self.window, text="보내는 사람의 이메일을 입력해주세요")
        sEmail.place(x=10, y=15)
        sPass = Label(self.window, text="보내는 사람의 비밀번호를 입력해주세요")
        sPass.place(x=10, y=40)
        rEmail = Label(self.window, text="받는 사람의 이메일을 입력해주세요")
        rEmail.place(x=10, y=100)

        self.sValue = StringVar() # 보내는 사람 이메일
        sTextbox = ttk.Entry(self.window, width=20, textvariable=self.sValue)
        sTextbox.place(x=240, y=15)
        self.pValue = StringVar() # 보내는 사람 비밀번호
        pTextbox = ttk.Entry(self.window, width=20, textvariable=self.pValue)
        pTextbox.place(x=240, y=40)
        self.rValue = StringVar() # 받는 사람 이메일
        rTextbox = ttk.Entry(self.window, width=20, textvariable=self.rValue)
        rTextbox.place(x=240, y=100)

        button = Button(self.window, text="보내기", width=10, command=self.send)
        button.place(x=150, y=150)

        self.window.mainloop()

    def send(self):
        # 여기에 보내는 코드만 추가하면 됨
        # self.rValue 이런 변수는 값을 받을 때 self.rValue.get()으로 값을 가져와서 해야함
        pass

# gmail파일 돌릴때 아래 주석 풀고
#main("테스트다")