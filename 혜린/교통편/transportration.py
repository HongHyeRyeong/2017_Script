import urllib.request  # 파이썬 2버전에서 urllib2
import xml.etree.ElementTree as etree

##### global
loopFlag = 1
tree = None

def printMenu():
    PLACE = str(input('문화공간 이름을 입력하세욘(종료는 q): '))
    if(PLACE=='q'):
        Quit()
    else:
        SearchPlace(PLACE)
    # print("==================")

def SearchPlace(PLACE):
# 파일 읽어오긔
    tree = etree.parse('transportration.xml')
    root = tree.getroot()
# 이름으로 검색하긔
    for a in root.findall('row'):
        if (a.findtext("FAC_NAME")==PLACE):
            print("장소:" + a.findtext("FAC_NAME"))
            print("*교통편 안내*")
            print(a.findtext("TRAFTYPE_NM"))
            print(a.findtext("TRAFINFO"))
            print("----------------------")


def CreateXML():
    key = '6e4e77665672696e3835725a787a62'
    url = "http://openAPI.seoul.go.kr:8088/" + key + "/xml/SearchCulturalFacilitiesTrafficService/1/5/"

    data = urllib.request.urlopen(url).read()
    f = open("transportration.xml", "wb")
    f.write(data)


def Quit():
    global loopFlag
    loopFlag = 0


while(loopFlag > 0):
    printMenu()

else:
    print ("앙뇽!")
