from tkinter import*
from tkinter import ttk

import xml.etree.ElementTree as ET
import webbrowser
import data
import gmail

class main:
    def __init__(self):
        self.myData = data.GetDataReservation()

        self.tree = ET.parse("xml/dataReservation.xml")
        self.root = self.tree.getroot()

        self.window = Tk()
        self.window.title("Reservation")
        self.window.geometry("500x600")

        self.listTitle = []

        self.rValue = IntVar()
        Radiobutton(self.window, text="문화 행사 전체 출력하기", variable=self.rValue, value=1).place(x=10, y=10)
        Radiobutton(self.window, text="문화 행사 검색해서 출력하기", variable=self.rValue, value=2).place(x=10, y=45)

        self.cValue = StringVar()
        combo = ttk.Combobox(self.window, width=5, textvariable=self.cValue, state="readonly")
        combo['values'] = ('Select', '장르', '제목')
        combo.place(x=30, y=80)
        combo.current(0)

        self.tValue = StringVar()
        print("000",self.tValue.get())
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
        self.listbox.bind("<Double-Button-1>", self.site)
        self.listbox.place(x=5, y=150)
        scrollbarX.config(command=self.listbox.yview)
        scrollbarY.config(command=self.listbox.xview)

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
            self.listTitle.append(i.findtext("SVCNM"))
            self.listbox.insert(cnt, "장르: "+i.findtext("MINCLASSNM")+"   제목: "+i.findtext("SVCNM")+
                                "   장소: "+i.findtext("PLACENM")+"비용: "+i.findtext("PAYATNM")+
                                "   접수 시작일"+i.findtext("RCPTBGNDT")+"   접수 종료일"+i.findtext("RCPTENDDT")+
                                "   예약 상태: : "+i.findtext("SVCSTATNM"))
            cnt += 1

    def selectSub(self):
        cnt = 0
        for i in self.root.iter("row"):
            if self.tValue.get() == i.findtext("MINCLASSNM"):
                self.listTitle.append(i.findtext("SVCNM"))
                self.listbox.insert(cnt, "장르: "+i.findtext("MINCLASSNM")+"   제목: "+i.findtext("SVCNM")+
                                    "   장소: "+i.findtext("PLACENM")+"비용: "+i.findtext("PAYATNM")+
                                    "   접수 시작일"+i.findtext("RCPTBGNDT")+"   접수 종료일"+i.findtext("RCPTENDDT")+
                                    "   예약 상태: : "+i.findtext("SVCSTATNM"))
                cnt += 1

    def selectTitle(self):
        cnt = 0
        for i in self.root.iter("row"):
            if self.tValue.get() == i.findtext("SVCNM"):
                self.listTitle.append(i.findtext("SVCNM"))
                self.listbox.insert(cnt, "장르: "+i.findtext("MINCLASSNM")+"   제목: "+i.findtext("SVCNM")+
                                    "   장소: "+i.findtext("PLACENM")+"비용: "+i.findtext("PAYATNM")+
                                    "   접수 시작일"+i.findtext("RCPTBGNDT")+"   접수 종료일"+i.findtext("RCPTENDDT")+
                                    "   예약 상태: : "+i.findtext("SVCSTATNM"))
                cnt += 1

    def site(self, event):
        idx = self.listbox.curselection()
        for i in self.root.iter("row"):
            if self.listTitle[idx[0]] == i.findtext("SVCNM"):
                webbrowser.open_new(i.findtext("SVCURL"))
                break

    def mail(self):
        idx = self.listbox.curselection()
        if len(idx) > 0:
            gmail.main(self.listbox.get(idx[0]))

# myMain = main()