with open('./pp_204_readtest.txt') as f:
    count = 0
    search = input()
    for line in f:
        if line.find(search):
            print('data is find.')
