from tkinter import *
import data

myData = data.GetDataSearch()
myData.main()

window = Tk()
window.title("문화 행사 정보")
window.geometry("600x800")

class print():
    global listbox

    listbox = Listbox(window)
    listbox.insert(1,"Python")
    listbox.insert(2,"Perl")
    listbox.insert(3,"C")
    listbox.insert(4,"PHP")
    listbox.insert(5,"JSP")
    listbox.insert(6,"Ruby")
    listbox.place(x=0, y=0)

# 배경
background = Frame(window)
background.pack()
img = PhotoImage(file='image/background.png')
imageLabel = Label(background, image=img)
imageLabel.image = img
imageLabel.pack()

# 메인 메뉴
bPrint = Button(window, text="전체 출력", width=10, command = print)
bPrint.place(x=10, y=80)
bSearch = Button(window, text="검색", width=10)
bSearch.place(x=130, y=80)
bReserve = Button(window, text="예약", width=10)
bReserve.place(x=250, y=80)
bTraffic = Button(window, text="교통편", width=10)
bTraffic.place(x=370, y=80)
bMail = Button(window, text="메일", width=10)
bMail.place(x=490, y=80)

window.mainloop()