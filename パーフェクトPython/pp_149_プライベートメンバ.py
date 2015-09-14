class ClassPrivate:
    pass

    def method_global(self):
        pass

    # __2つを先頭に付与したメソッドはプライベート扱いとなる。
    def __method_private(self):
    	print('__method_private is called.')

    def call_private(self):
    	self.__method_private()

c = ClassPrivate()
c.method_global()
c.call_private()
