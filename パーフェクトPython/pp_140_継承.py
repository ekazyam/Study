class Base:
    pass

    def echo_test(self, data):
        print('引数は', data, 'です')

    def echo_test2(self):
        print('普通のecho1です')

    def echo_test3(self):
        print('普通のecho2です')


class Base2:

    def echo_test4(self):
        print('多重継承のテストです。')


class NewClass(Base, Base2):

    def echo_test(self, data='None'):
        # 基底クラスで定義されたメソッドを呼び出すにはsuper()を使うこと。
        data = data + '+'
        super().echo_test(data)

if __name__ == '__main__':
    a = NewClass()
    a.echo_test('DATA')
    a.echo_test()
    a.echo_test2()

    b = NewClass()
    b.echo_test()
    b.echo_test4()
