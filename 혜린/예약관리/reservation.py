import urllib.request  # 파이썬 2버전에서 urllib2
import xml.etree.ElementTree as etree

##### global
loopFlag = 1
tree = None

def printMenu():
    print("========Menu==========")
    print("예약 바로가기 서비스입니다!")
    print("종료:   q")
    print("전체 공연 정보: p")
    print("이름으로 검색: n")
    print("소분류로 검색: c")
    print("======================")

def launcherFunction(menu):
    if menu == 'l':
        CreateXML()
    elif menu == 'q':
        Quit()
    elif menu == 'p':
        PrintALL()
    elif menu == 'n':
        NAME = str(input('문화행사 이름? :'))
        SearchByPlace(NAME)
    elif menu == 'c':
        SearchByCategory()
    else:
        print("error : 유효하지 않음")

#소분류로 검색
def SearchByCategory():
    category = int(input('분류(공연/콘서트 = 1, 행사/대회 = 2  문화관광=3 전시/관람=4): '))
    if category < 5:
        tree = etree.parse('reservation.xml')
        root = tree.getroot()
        if category == 1:
            category = '공연/콘서트'
        elif category == 2:
            category = '행사/대회'
        elif category == 3:
            category = '문화관광'
        elif category == 4:
            category = '전시/관람'

        for a in root.findall('row'):
            if (a.findtext("MINCLASSNM") == category):
                print("행사명: " + a.findtext("SVCNM"))
                print("소분류: " + a.findtext("MINCLASSNM"))
                print("장소: " + a.findtext("PLACENM"))
                print("비용: " + a.findtext("PAYATNM"))
                print("예약상태: : " + a.findtext("SVCSTATNM"))
                print("예약바로가기: " + a.findtext("SVCURL"))
                print("=================================")

    else:
        print("error: 1,2,3,4")
        SearchByCategory()



def SearchByPlace(NAME):
# 파일 읽어오긔
    tree = etree.parse('reservation.xml')
    root = tree.getroot()
# 이름으로 검색하긔
    for a in root.findall('row'):
      if (a.findtext("SVCNM")==NAME):
        print("행사명: " + a.findtext("SVCNM"))
        print("장소: " + a.findtext("PLACENM"))
        print("비용: " + a.findtext("PAYATNM"))
        print("소분류: " + a.findtext("MINCLASSNM"))
        print("예약상태: : " + a.findtext("SVCSTATNM"))
        print("예약바로가기: " + a.findtext("SVCURL"))
        print("=================================")

def PrintALL():
    tree = etree.parse('reservation.xml')
    root = tree.getroot()
    for a in root.findall('row'):
        print("행사명: " + a.findtext("SVCNM"))
        print("장소: " + a.findtext("PLACENM"))
        print("비용: " + a.findtext("PAYATNM"))
        print("소분류: " + a.findtext("MINCLASSNM"))
        print("예약상태: : " + a.findtext("SVCSTATNM"))
        print("예약바로가기: " + a.findtext("SVCURL"))
        print("=================================")


def CreateXML():
    key = '6e4e77665672696e3835725a787a62'
    url = "http://openAPI.seoul.go.kr:8088/" + key + "/xml/ListPublicReservationCulture/1/52/"

    data = urllib.request.urlopen(url).read()
    f = open("reservation.xml", "wb")
    f.write(data)


def Quit():
    global loopFlag
    loopFlag = 0


while(loopFlag > 0):
    printMenu()
    MENU = str(input('select MENU :'))
    launcherFunction(MENU)


else:
    print ("앙뇽!")



