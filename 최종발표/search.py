from tkinter import*
from tkinter import ttk

import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

import xml.etree.ElementTree as ET
import data
import gmail


#global value
host = "smtp.gmail.com" # Gmail STMP 서버 주소.
port = "587"
htmlFileName = "logo.html"

class main:
    def __init__(self):
        self.myData = data.GetDataSearch()

        self.tree = ET.parse("xml/dataSearch.xml")
        self.root = self.tree.getroot()

        self.window = Tk()
        self.window.title("Search")
        self.window.geometry("500x600")

        self.rValue = IntVar()
        Radiobutton(self.window, text="문화 행사 전체 출력하기", variable=self.rValue, value=1).place(x=10, y=10)
        Radiobutton(self.window, text="문화 행사 검색해서 출력하기", variable=self.rValue, value=2).place(x=10, y=45)

        self.cValue = StringVar()
        combo = ttk.Combobox(self.window, width=5, textvariable=self.cValue, state="readonly")
        combo['values'] = ('Select', '장르', '제목')
        combo.place(x=30, y=80)
        combo.current(0)

        self.tValue = StringVar()
        textbox = ttk.Entry(self.window, width=20, textvariable=self.tValue)
        textbox.place(x=105, y=80)

        sButton = Button(self.window, text="검색", width=4, command=self.select)
        sButton.place(x=350, y=110)

        eButton = Button(self.window, text="메일", width=4, command=self.mail)
        eButton.place(x=410, y=110)


        scrollbarX = Scrollbar(self.window)
        scrollbarX.pack(side=RIGHT, fill=Y)
        scrollbarY = Scrollbar(self.window, orient='horizontal')
        scrollbarY.pack(side=BOTTOM, fill=X)
        self.listbox = Listbox(self.window, width=65, height=25,
                               yscrollcommand=scrollbarX.set, xscrollcommand=scrollbarY.set)
        self.listbox.place(x=5, y=150)
        scrollbarX.config(command=self.listbox.yview)
        scrollbarY.config(command=self.listbox.xview)

        self.listTitle = []

        self.window.mainloop()

    def select(self):
        self.listbox.delete(0, self.listbox.size())
        self.listTitle.clear()
        if self.rValue.get() == 1:
            self.printAll()
        elif self.rValue.get() == 2:
            if self.cValue.get() == '장르':
                self.selectSub()
            elif self.cValue.get() == '제목':
                self.selectTitle()

    def printAll(self):
        cnt = 0
        for i in self.root.iter("row"):
            self.listTitle.append(i.findtext("TITLE"))
            self.listbox.insert(cnt, "장르: "+i.findtext("CODENAME")+"   제목: "+i.findtext("TITLE")
                           +"   시작일: "+i.findtext("STRTDATE")+"   종료일: "+ i.findtext("END_DATE")
                           +"   시간: "+i.findtext("TIME")+"   장소: "+i.findtext("PLACE")+"   이용대상: "+i.findtext("USE_TRGT"))
            cnt += 1

    def selectSub(self):
        cnt = 0
        for i in self.root.iter("row"):
            if self.tValue.get() == i.findtext("CODENAME"):
                self.listTitle.append(i.findtext("TITLE"))
                self.listbox.insert(cnt, "장르: "+i.findtext("CODENAME")+"   제목: "+i.findtext("TITLE")
                               +"   시작일: "+i.findtext("STRTDATE")+"   종료일: "+ i.findtext("END_DATE")
                               +"   시간: "+i.findtext("TIME")+"   장소: "+i.findtext("PLACE")+"   이용대상: "+i.findtext("USE_TRGT"))
                cnt += 1

    def selectTitle(self):
        cnt = 0
        for i in self.root.iter("row"):
            if self.tValue.get() == i.findtext("TITLE"):
                self.listTitle.append(i.findtext("TITLE"))
                self.listbox.insert(cnt, "장르: "+i.findtext("CODENAME")+"   제목: "+i.findtext("TITLE")
                               +"   시작일: "+i.findtext("STRTDATE")+"   종료일: "+ i.findtext("END_DATE")
                               +"   시간: "+i.findtext("TIME")+"   장소: "+i.findtext("PLACE")+"   이용대상: "+i.findtext("USE_TRGT"))
                cnt += 1

    def mail(self):
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


        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = "Test email in Python 3.0"
        msg['From'] = senderID
        msg['To'] = receiver

        # MIME 문서를 생성한다.
        htmlFD = open(htmlFileName, 'rb')
        HtmlPart = MIMEText(htmlFD.read(), 'html', _charset='UTF-8')
        htmlFD.close()

        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        msg.attach(HtmlPart)

        # 메일을 발송한다.
        s = mysmtplib.MySMTP(host, port)

        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderID,senderPW)
        s.sendmail(senderID, receiver, msg.as_string())
        s.close()










        idx = self.listbox.curselection()
        if len(idx) > 0:
            gmail.main(self.listbox.get(idx[0]),self.sValue.get(),self.pValue.get(),self.rValue.get())



main()