class PropertyTest():
    def __init__(self, data=None):
        self.__data = data

    def setData(self, data=None):
        self.__data = data

    def getData(self):
        return self.__data

# メソッド経由でset/getを実行する。(今まで通り)
p = PropertyTest()
p.setData('aaaa')
print(p.getData())
