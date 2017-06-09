import urllib.request

def GetDataSearch():
    key = "7552447341686c303733527371514a"
    url = 'http://openAPI.seoul.go.kr:8088/7552447341686c303733527371514a/xml/SearchConcertDetailService/1/999/'

    data = urllib.request.urlopen(url).read()
    f = open("xml/dataSearch.xml","wb")
    f.write(data)
    f.close()

def GetDataReservation():
    key = '6e4e77665672696e3835725a787a62'
    url = "http://openAPI.seoul.go.kr:8088/" + key + "/xml/ListPublicReservationCulture/1/52/"

    data = urllib.request.urlopen(url).read()
    f = open("xml/dataReservation.xml", "wb")
    f.write(data)
    f.close()

def GetDataTransportration():
    key = '6e4e77665672696e3835725a787a62'
    url = "http://openAPI.seoul.go.kr:8088/" + key + "/xml/SearchCulturalFacilitiesTrafficService/1/999/"

    data = urllib.request.urlopen(url).read()
    f = open("xml/dataTransportration.xml", "wb")
    f.write(data)
    f.close()

def GetDataXY():     #좌표 받아오는 함수
    key = '6e4e77665672696e3835725a787a62'
    url = "http://openAPI.seoul.go.kr:8088/"+key+"/xml/SearchCulturalFacilitiesDetailService/1/490/"

    data = urllib.request.urlopen(url).read()
    f = open("xml/dataXY.xml", "wb")
    f.write(data)
    f.close()