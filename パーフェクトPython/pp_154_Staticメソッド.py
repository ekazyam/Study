class StaticClass:
    pass

    @staticmethod
    def static_method():
        print('static_method is called.')

c = StaticClass()
c.static_method()
