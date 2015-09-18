class MethodTest:

    class_data_1 = None
    class_data_2 = None

    # コンストラクタ
    def __init__(self, data1='DefaultData1', data2='DefaultData2'):
        self.class_data_1 = data1
        self.class_data_2 = data2

    # デストラクタ
    def __del__(self):
        print('Deleted.')

    def test(self, arg):
        print(self.class_data_1)
        print(self.class_data_2)
        print(arg)


if __name__ == '__main__':
    class_test = MethodTest('DefineData')
    class_test.test(2)
