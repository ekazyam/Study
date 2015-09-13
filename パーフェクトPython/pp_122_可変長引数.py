def function(*arg, *):
    for i in arg:
        print(i)

# 可変長の引数を関数に渡せる
if __name__ == '__main__':
    function(1, 2, 3, 4)
