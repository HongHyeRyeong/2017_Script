import urllib.request  # 파이썬 2버전에서 urllib2
import xml.etree.ElementTree as etree
import xml.parsers.expat


class GetData:
    terNum='1'
    date='20170527'
    hour='15'

    key='Ee%2BAvKekFDSqObljJovZ%2B%2Fyg1SC21PhJjj%2FkqZiwWvYOwgwKn85tE2HfkztQx8407%2Fj8hkWuQSROspb6%2B3S56Q%3D%3D'

    url="http://openapi.airport.co.kr/service/rest/dailyExpectPassenger/dailyExpectPassenger?serviceKey="
    Fullurl=url+key+"&schDate="+date+"&schAirport"+"=GMP&schTof=I&schHH="+hour

    # url="http://openapi.airport.kr/openapi/service/StatusOfDepartures/getDeparturesCongestion?ServiceKey="
    # Fullurl=url+key+"&terno="+terNum
    # 링크로 직접 들어가지는 건 되는데 이 방법으로는 에러..

    print(Fullurl)

    def extract(text, sub1, sub2):
        """
        extract a substring from text between first
        occurances of substrings sub1 and sub2
        """
        return text.split(sub1, 1)[-1].split(sub2, 1)[0]

    def main(self):
        data=urllib.request.urlopen(self.Fullurl).read()
        f = open("congestion.xml","wb")
        f.write(data)

        def start_element(name, attrs):
            print ('Start element:',(name))

        def char_data(data):
            print('Character data:',repr(data))
            print('-----------------------------')


        pa=xml.parsers.expat.ParserCreate()
        pa.StartElementHandler = start_element
        pa.CharacterDataHandler=char_data
        pa.Parse(data)


        # tree = etree.parse('congestion.xml')
        # root = tree.getroot()
        # for a in root.findall('terno'):


getData=GetData()
getData.main()
