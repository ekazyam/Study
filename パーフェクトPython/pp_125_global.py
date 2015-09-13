def function():
    # ここでどのval変数を使うか指定する。
    # globalを指定することで、外部で定義された変数へのアクセスを可能とする。
    global val
    val = 'change'
    print(val)

val = 'original'
function()
print(val)
