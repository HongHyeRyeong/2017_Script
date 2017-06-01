from tkinter import*
from tkinter import ttk

import xml.etree.ElementTree as ET
import data

class main:
    def __init__(self):
        self.myData = data.GetDataTransportration()

        self.tree = ET.parse("xml/dataTransportration.xml")
        self.root = self.tree.getroot()

        self.window = Tk()
        self.window.title("Transportration")
        self.window.geometry("500x600")

        lPlace = Label(self.window, text="검색할 장소를 입력해주세요")
        lPlace.place(x=10, y=10)

        self.tValue = StringVar()
        textbox = ttk.Entry(self.window, width=20, textvariable=self.tValue)
        textbox.place(x=230, y=10)

        sButton = Button(self.window, text="검색", width=4, command=self.select)
        sButton.place(x=290, y=70)

        # 메일 추가
        eButton = Button(self.window, text="메일", width=4, command=self.mail)
        eButton.place(x=350, y=70)

        # 지도 추가
        mButton = Button(self.window, text="지도", width=4, command=self.map)
        mButton.place(x=410, y=70)

        scrollbarX = Scrollbar(self.window)
        scrollbarX.pack(side=RIGHT, fill=Y)
        scrollbarY = Scrollbar(self.window, orient='horizontal')
        scrollbarY.pack(side=BOTTOM, fill=X)
        self.listbox = Listbox(self.window, width=58, height=21,
                               yscrollcommand=scrollbarX.set, xscrollcommand=scrollbarY.set)
        self.listbox.place(x=5, y=120)
        scrollbarX.config(command=self.listbox.yview)
        scrollbarY.config(command=self.listbox.xview)

        self.window.mainloop()

    def select(self):
        self.listbox.delete(0, self.listbox.size())

        cnt = 0
        for i in self.root.iter('row'):
            if self.tValue.get() == i.findtext("FAC_NAME"):
                self.listbox.insert(cnt,i.findtext("TRAFTYPE_NM")+" - "+i.findtext("TRAFINFO"))
                cnt += 1

    def map(self):
        pass

    # 메일 코드 추가
    def mail(self):
        pass

#myMain = main()