x = { 1 ,2 ,3 ,4 ,4 , 4, 6}
#set型は、重複を取り除いたリストを作成してくれる
print(x)

x.add(5)
x.add(5)
x.add(5)
print(x)

x.remove(1)
print(x)

x.discard(5)
