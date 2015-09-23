if __name__ == '__main__':
    # 全行を読み込む
    f = open('./pp_204_readtest.txt')
    print(f.read(), end="")
    f.close()

    f = open('./pp_204_readtest.txt')

    # ループで処理する
    for line in f:
        print(line, end="")

    f.close()
