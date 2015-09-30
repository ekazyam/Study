import atexit


def show_message(f):
    """関数デコレータのテスト"""
    print('show_message関数です。')

    def wrapper():
        print("ここは関数デコレータで定義したメッセージです。")
        return f()

    return wrapper


def show_message2(f):
    """関数デコレータのテスト"""
    def wrapper():
        print("ここは関数デコレータで定義したメッセージ2です。")
        return f()

    return wrapper


@show_message
@show_message2
def testfunc():
    print('テストファンクションが呼ばれました。')
    return 'これはリターン値です。'


@atexit.register
def exitfunc():
    print('関数が終了しました。')

testfunc()
