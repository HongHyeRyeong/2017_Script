from tkinter import*
from tkinter import ttk

import xml.etree.ElementTree as ET
import data
import webbrowser
import gmail

class main:
    def __init__(self):
        self.myData = data.GetDataTransportration()
        self.tree = ET.parse("xml/dataTransportration.xml")
        self.root = self.tree.getroot()

        self.window = Tk()
        self.window.title("Transportration")
        self.window.geometry("500x370")

        lPlace = Label(self.window, text="검색할 장소를 입력해주세요")
        lPlace.place(x=10, y=10)

        self.tValue = StringVar()
        textbox = ttk.Entry(self.window, width=20, textvariable=self.tValue)
        textbox.place(x=200, y=10)

        sButton = Button(self.window, text="검색", width=4, command=self.select)
        sButton.place(x=350, y=50)
        # 지도 추가
        mButton = Button(self.window, text="지도", width=4, command=self.map)
        mButton.place(x=410, y=50)

        scrollbarX = Scrollbar(self.window)
        scrollbarX.pack(side=RIGHT, fill=Y)
        scrollbarY = Scrollbar(self.window, orient='horizontal')
        scrollbarY.pack(side=BOTTOM, fill=X)
        self.listbox = Listbox(self.window, width=65, height=15,
                               yscrollcommand=scrollbarX.set, xscrollcommand=scrollbarY.set)
        self.listbox.place(x=5, y=90)
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
        mapOK=FALSE
        #self.Data = data.GetDataXY()
        self.tree2 = ET.parse("xml/dataXY.xml")  # 좌표 정보
        self.root2 = self.tree2.getroot()

        for i in self.root2.iter('row'):
            if self.tValue.get() == i.findtext("FAC_NAME"):
                mapOK=TRUE
                X = i.findtext("X_COORD")
                Y = i.findtext("Y_COORD")
                url = "https://maps.googleapis.com/maps/api/staticmap?center=" + X + "," + Y + "&zoom=17&size=2048x2048&markers=color:blue%7Clabel:HERE%7C"+X+","+Y
                webbrowser.open_new(url)

        if FALSE==mapOK:
            print("지도가 준비되어있지 않습니다.")
            #메세지창 띄우기


#myMain = main()