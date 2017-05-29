import xml.etree.ElementTree as ET
import data

class Menu:
    def __init__(self):
        data.GetDataSearch()
        data.GetDataReservation()
        data.GetDataTransportration()

        self.treeS = ET.parse("xml/dataSearch.xml")
        self.rootS = self.treeS.getroot()
        self.treeR = ET.parse("xml/reservation.xml")
        self.rootR = self.treeR.getroot()
        self.treeT = ET.parse("xml/transportration.xml")
        self.rootT = self.treeT.getroot()

    def main(self):
        while True:
            print("===========================================")
            print("서울시 문화행사 정보")
            print("1. Print - 전체 정보 출력")
            print("2. Search - 장르, 제목 검색")
            print("3. Reservation - 예약 바로가기")
            print("4. Transportration - 교통편 안내")
            print("0. Exit - 프로그램 종료")
            numM = int(input("메뉴를 입력해주세요: "))
            print("===========================================")

            if numM == 1:
                self.Print()
            elif numM == 2:
                self.Search()
            elif numM == 3:
                self.Reservation()
            elif numM == 4:
                self.Transportration()
            elif numM == 0:
                print("프로그램을 종료합니다.")
                break;

            else:
                print("다시 입력해주세요!")

    def Print(self):
        for i in self.rootS.iter("row"):
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

        for i in self.rootS.iter("row"):
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

        for i in self.rootS.iter("row"):
            if(a == i.findtext("TITLE")):
                print("장르:",i.findtext("CODENAME"))
                print("제목:",i.findtext("TITLE"))
                print("시작일:",i.findtext("STRTDATE"),
                      "종료일:",i.findtext("END_DATE"))
                print("시간:",i.findtext("TIME"))
                print("장소:",i.findtext("PLACE"))
                print("이용대상:",i.findtext("USE_TRGT"))
                print("-------------------------------------------")

    def Reservation(self):
            while True:
                print("Reservation를 선택하셨습니다.")
                print("1. 전체 문화 행사 정보")
                print("2. 장르로 검색해 예약하기")
                print("3. 제목으로 검색해 예약하기")
                print("0. Exit")
                numS = int(input("어떤 것을 검색하시겠습니까? "))
                print("===========================================")
                if numS == 1:
                    self.ReservationPrint()
                    break
                elif numS == 2:
                    self.ReservationCodename()
                    break
                elif numS == 3:
                    self.ReservationTitle()
                    break
                elif numS == 0:
                    print("초기메뉴로 돌아갑니다.")
                    break
                else:
                    print("다시 입력해주세요!")

    def ReservationPrint(self):
        for a in self.rootR.iter('row'):
            print("행사명: " + a.findtext("SVCNM"))
            print("장소: " + a.findtext("PLACENM"))
            print("비용: " + a.findtext("PAYATNM"))
            print("소분류: " + a.findtext("MINCLASSNM"))
            print("접수 시작일", a.findtext("RCPTBGNDT"), " 접수 종료일", a.findtext("RCPTENDDT"))
            print("예약 상태: : " + a.findtext("SVCSTATNM"))
            print("예약 바로가기: " + a.findtext("SVCURL"))
            print("-------------------------------------------")

    def ReservationCodename(self):
        print("1. 공연/콘서트")
        print("2. 행사/대회")
        print("3. 문화관광")
        print("4. 전시/관람")
        category = int(input("어떤 것을 검색하시겠습니까? "))

        if category < 5:
            if category == 1:
                category = '공연/콘서트'
            elif category == 2:
                category = '행사/대회'
            elif category == 3:
                category = '문화관광'
            elif category == 4:
                category = '전시/관람'

            for a in self.rootR.iter('row'):
                if (a.findtext("MINCLASSNM") == category):
                    print("행사명: " + a.findtext("SVCNM"))
                    print("소분류: " + a.findtext("MINCLASSNM"))
                    print("장소: " + a.findtext("PLACENM"))
                    print("비용: " + a.findtext("PAYATNM"))
                    print("접수 시작일", a.findtext("RCPTBGNDT"), " 접수 종료일", a.findtext("RCPTENDDT"))
                    print("예약 상태: : " + a.findtext("SVCSTATNM"))
                    print("예약 바로가기: " + a.findtext("SVCURL"))
                    print("-------------------------------------------")

        else:
            print("다시 입력해주세요!")
            self.ReservationCodename()

    def ReservationTitle(self):
        name = str(input('제목을 입력하세요 :'))

        for a in self.rootR.iter('row'):
          if (a.findtext("SVCNM") == name):
              print("행사명: " + a.findtext("SVCNM"))
              print("장소: " + a.findtext("PLACENM"))
              print("비용: " + a.findtext("PAYATNM"))
              print("소분류: " + a.findtext("MINCLASSNM"))
              print("접수 시작일", a.findtext("RCPTBGNDT"), " 접수 종료일", a.findtext("RCPTENDDT"))
              print("예약 상태: : " + a.findtext("SVCSTATNM"))
              print("예약 바로가기: " + a.findtext("SVCURL"))
              print("-------------------------------------------")

    def Transportration(self):
        PLACE = str(input('장소를 입력하세요: '))

        for a in self.rootT.iter('row'):
            if (a.findtext("FAC_NAME") == PLACE):
                print(a.findtext("TRAFTYPE_NM")," - ", a.findtext("TRAFINFO"))

myMenu = Menu()
myMenu.main()