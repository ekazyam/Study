def function1():
    var1 = 'function1のデータ'

    def function2():
        nonlocal var1
        var1 = 'function2で書き換え'
        var2 = 'function2のデータ'
        print(var1)
        print(var2)

    function2()

    print(var1)

function1()
