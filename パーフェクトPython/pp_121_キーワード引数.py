def keyword(arg1=1, arg2=2, arg3=3, arg4=4):
    print('datais')
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

if __name__ == '__main__':
    keyword(1, 2, arg4=99)
    keyword()

    # keyword指定
    a = {'arg1': 2, 'arg4': 10}
    keyword(**a)

    # 位置指定
    b = (22, None, 33)
    keyword(*b)
