# @propertyを使用したスマートなclass
class PropertyTest2():
    __data = None

    def __init__(self, data=None):
        self.__data = data

    # getter扱い
    @property
    def data(self):
        return self.__data

    # setter扱い
    @data.setter
    def data(self, value):
        self.__data = value

    # deleter扱い
    @data.deleter
    def data(self):
        del self.__data

p = PropertyTest2(123)
print(p.data)
p.data = 234
print(p.data)
