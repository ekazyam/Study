def is_odd(item):
    return item % 2 == 1

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
ret = filter(is_odd, a)

print(ret)
