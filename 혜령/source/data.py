import urllib.request

class GetDataSearch:
    key = "7552447341686c303733527371514a"
    url = 'http://openAPI.seoul.go.kr:8088/7552447341686c303733527371514a/xml/SearchConcertDetailService/1/999/'

    def main(self):
        data = urllib.request.urlopen(self.url).read()
        f = open("xml/dataSearch.xml","wb")
        f.write(data)
        f.close()