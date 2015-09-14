class ClassMethod:

    def normal_method(self):
        print('normal_method')

    @classmethod
    def class_method(self):
        print('class_method')

c = ClassMethod()
c.normal_method()
# Classメソッドはインスタンス生成してもしなくても呼べる
ClassMethod.class_method()
c.class_method()
