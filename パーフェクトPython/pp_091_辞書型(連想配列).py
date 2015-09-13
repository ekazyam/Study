def dictest(key='def_key'):
    a = {'key1': 'testval1', 'key2': 'testval2', 'key3': 'testval3'}
    print(a['key1'])
    print(a['key2'])

    if(key in a):
        print("exist.")
    else:
        print('not exist')
        # デフォルトのキー値を指定して辞書型リストからデータを取得する
        print(a.get('key1'))

    print('データのイテレーションアクセステスト')
    for x in a:
        print(a[x])

    print('データのイテレーションアクセステスト(値直接指定)')
    for key, value in a.items():
        print(key, value)

    # データの更新
    a['key1'] = 'NewData'
    print(a)

    # データの削除
    a.pop('key1')
    print(a)

if __name__ == '__main__':
    # key値の確認
    key = 'key1'
    dictest(key)
    dictest()
