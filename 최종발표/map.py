import xml.etree.ElementTree as ET
import urllib.request
import data

class map:
    def __init__(self,X,Y):
        #self.myData = data.GetDataXY()
        # self.tree = ET.parse("xml/dataXY.xml")
        # self.root = self.tree.getroot()
        # # PLACENAME=input("장소이름을 입력하시오:")
        # for i in self.root.iter("row"):
        #     if PLACENAME==i.findtext("FAC_NAME"):
        #         X=i.findtext("X_COORD")
        #         Y=i.findtext("Y_COORD")
        self.draw(X,Y)

    def draw(self,X,Y):
        url= "https://maps.googleapis.com/maps/api/staticmap?center="+X+","+Y+"&zoom=15&size=2048x2048"
        print(url)
