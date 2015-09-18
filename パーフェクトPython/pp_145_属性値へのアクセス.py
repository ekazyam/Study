class test:
    aaa = None

    def __init__(self, arg):
        self.aaa = arg
        print(self.aaa)

fn_test = test('testtest')

print(fn_test.aaa)
