#!/usr/bin/env python

# main class definition.
"""
here is docstring.
"""


class main():

    __data = ''
    __iterate = [1, 2, 3, 4, 5, 6]
    __set = {1, 2, 3, 4, 5, 6}
    __taple = (1, 2, 3, 4, 5, 6)

    def __init__(self, input_data='default_value'):
        self.data = input_data

    def main(self):
        print(self.data)

    def iterate(self):
        for data in self.__iterate:
            print('iterate is ', data)

    def set(self):
        for data in self.__set:
            print('set is ', data)

    def taple(self):
        for data in self.__taple:
            print('taple is ', data)

    def is_even(self, data):
        return data % 2 == 0

    def is_odd(self, data):
        return data % 2 != 0

    def even_or_odd(self, func, data):
        if func(data):
            return true
        return false

# check main funciton
if __name__ == '__main__':
    # create test class instance.
    test_class = main()
    test_class.main()

    # create test class instance2.
    test_class_2 = main('dammy_data')
    test_class_2.main()

    # iterate
    test_class_2.iterate()

    # set.
    test_class_2.set()

    # taple
    test_class.taple()

    # doc string.
    # help(test_class)
    # help(test_class_2)

    # try except
    try:
        print(not_define)
    except:
        print('not_define is not defined variables.')
    finally:
        print('finally processing')

    even_or_odd(test_class.is_even,2)
