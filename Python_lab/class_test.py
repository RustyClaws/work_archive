class test:
    name = 'xiaoming'
    age = 114514
    def fun(self):      # self 表示实例
        return f"hello, I am {test.name}"

my_class = test()
# 先实例化，一切初始化，防止脏数据
print("test.name = ", my_class.name)
print("test.age = ", my_class.age)
print("test.fun() = ", my_class.fun())

print("===========")

class class_2:
    def __init__(self, para_a, Para_b):
        self.a = para_a
        self.b = Para_b

test_class = class_2(1145,14)
print("testclass.a and .b are:",test_class.a, test_class.b)

# 有self表示类的实例，是与普通函数区分的标志(self不是关键字，可以换别的，但一般不换)

class noob01:
    def nob(self):
        print(self)
        print(self.__class__)
t = noob01()
t.nob()


class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')

class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')

c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
# super ： 调用父类
# __XXX 表示私有函数，外部不能调用， 这种不是：__XXX__， 这种是类的专有方法
