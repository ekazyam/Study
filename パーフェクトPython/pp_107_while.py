# while文を抜けた瞬間にelse文に入る
# ただし、breakで抜けた時は無視される


def listcreate():
    i = 0
    while i < 10:
        if (i == 10):
            break
        else:
            print('i is ', i)
            i += 1
    else:
        print('else state.')


listcreate()
