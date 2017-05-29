import xml.etree.ElementTree as ET
import data

class Menu:
    def __init__(self):
        myData = data.GetDataSearch()
        myData.main()

        self.tree = ET.parse("xml/dataSearch.xml")
        self.root = self.tree.getroot()

    def main(self):
        while True:
            print("서울시 문화행사 정보")
            print("1. Print - 전체 정보 출력")
            print("2. Search - 장르, 제목 검색")
            print("0. Exit - 프로그램 종료")
            numM = int(input("메뉴를 입력해주세요: "))
            print("===========================================")

            if numM == 1:
                self.Print()
            elif numM == 2:
                self.Search()
            elif numM == 0:
                print("프로그램을 종료합니다.")
                break;

            else:
                print("다시 입력해주세요!")

    def Print(self):
        for i in self.root.iter("row"):
            print("장르:",i.findtext("CODENAME"))
            print("제목:",i.findtext("TITLE"))
            print("시작일:",i.findtext("STRTDATE"),
                  "종료일:",i.findtext("END_DATE"))
            print("시간:",i.findtext("TIME"))
            print("장소:",i.findtext("PLACE"))
            print("이용대상:",i.findtext("USE_TRGT"))
            print("-------------------------------------------")

    def Search(self):
            while True:
                print("Search를 선택하셨습니다.")
                print("1. 장르")
                print("2. 제목")
                print("0. Exit")
                numS = int(input("어떤 것을 검색하시겠습니까? "))
                print("===========================================")
                if numS == 1:
                    self.SearchCodename()
                    break
                elif numS == 2:
                    self.SearchTitle()
                    break
                elif numS == 0:
                    print("초기메뉴로 돌아갑니다.")
                    break
                else:
                    print("다시 입력해주세요!")

    def SearchCodename(self):
        a = input("장르를 입력해주세요: ")

        for i in self.root.iter("row"):
            if(a == i.findtext("CODENAME")):
                print("장르:",i.findtext("CODENAME"))
                print("제목:",i.findtext("TITLE"))
                print("시작일:",i.findtext("STRTDATE"),
                      "종료일:",i.findtext("END_DATE"))
                print("시간:",i.findtext("TIME"))
                print("장소:",i.findtext("PLACE"))
                print("이용대상:",i.findtext("USE_TRGT"))
                print("-------------------------------------------")

    def SearchTitle(self):
        a = input("공연 제목을 입력해주세요: ")

        for i in self.root.iter("row"):
            if(a == i.findtext("TITLE")):
                print("장르:",i.findtext("CODENAME"))
                print("제목:",i.findtext("TITLE"))
                print("시작일:",i.findtext("STRTDATE"),
                      "종료일:",i.findtext("END_DATE"))
                print("시간:",i.findtext("TIME"))
                print("장소:",i.findtext("PLACE"))
                print("이용대상:",i.findtext("USE_TRGT"))
                print("-------------------------------------------")

myMenu = Menu()
myMenu.main()