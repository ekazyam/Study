class TestClass:
    testprop = 0

    def getData(self):
        print(self.testprop)


if __name__ == '__main__':
    test = TestClass
    test()

    test.getData(test)
