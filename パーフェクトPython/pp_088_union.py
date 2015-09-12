def uniontest():
    a = {1,2,3,4,5}
    b = {6,7,8,9,10}
    print(a)
    print(b)
    c =a.union(b)
    print(c)

if __name__ == '__main__':
    # unionは非破壊的メソッドなので、別のオブジェクトに代入しないと消えます。
    uniontest()
    