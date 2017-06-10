from tkinter import*
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText

class main:
    def __init__(self, message):
        self.window = Tk()
        self.window.title("Gmail")
        self.window.geometry("400x100")

        self.message = message

        rEmail = Label(self.window, text="받는 사람의 이메일을 입력해주세요")
        rEmail.place(x=10, y=10)

        self.rValue = StringVar() # 받는 사람 이메일
        self.rTextbox = ttk.Entry(self.window, width=20, textvariable=self.rValue)
        self.rTextbox.place(x=240, y=10)

        button = Button(self.window, text="보내기", width=10, command=self.send)
        button.place(x=150, y=60)

        self.window.mainloop()

    def send(self):
        msg = MIMEText(self.message, "html", _charset="utf-8")

        msg['Subject'] = '문화행사 정보'
        msg['From'] = "ta722blo@gmail.com"
        msg['To'] = self.rValue.get()

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()

        s.login("ta722blo@gmail.com","12345qwert!")
        s.sendmail("ta722blo@gmail.com", self.rValue.get(), msg.as_string())
        s.quit()

        self.rTextbox.delete(0, END)