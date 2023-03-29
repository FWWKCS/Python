class property():
    global propertyList
    propertyList = []

    def __init__(self, data):
        self.data = data
        propertyList.append(' '.join(data))


    def GetList(self):
        print(f"총 {len(propertyList)}대의 매물이 있습니다.")
        for i in propertyList:
            print(i)

houseProperty = property(['강남아파트','매매','10억','2010년'])
houseProperty = property(['마표 오피스텔','전세','5억','2007년'])
houseProperty = property(['송파 빌라','월세','500/50','2000년'])

houseProperty.GetList()
