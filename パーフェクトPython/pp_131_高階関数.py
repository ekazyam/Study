def is_odd(item):
    return item % 2 == 1


def is_even(item):
    return item % 2 == 0


def filter(pred, seq):
    ret = []
    for item in seq:
        if pred(item):
            ret.append(item)
    return ret

a = [1, 2, 3, 4, 5, 6, 7, 8]
# 第一引数：is_odd関数を引数として渡す。
# これは、関数もオブジェクトであるというpythonの概念に基づき、
# 通常の変数と同じ様に関数の引数として関数を渡すテクニックである。
# ストラテジーパターンというデザインパターンの一種はこの機能を利用したものである。
ret = filter(is_odd, a)
print(ret)
ret = filter(is_even, a)
print(ret)



def documentation():
    pass
