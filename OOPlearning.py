class Cat():

    pass
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("猫在吃鱼")
    def show(self):
        print(self.name)
#第二种定义类的方式
def call(self):
    print("汪汪")
Dog=type("Dog",(object,),{'call':call})

smalldog=Dog()
smalldog.call()

smallcat=Cat("lili")
smallcat.show()
smallcat.eat()

class Blackcat(Cat):
    pass

    def eat(self):
        super().eat()
        print("黑猫捉老鼠")
class Yellocat(Cat):
    def eat(self):
        super().eat()
        print("黄猫扰小鸡")
    pass

def objeat(cal):
    cal.eat()

bigcat=Blackcat("dd")
bigcat.show()
bigcat.eat()
middlecat=Yellocat("cc")

objeat(bigcat)
objeat(middlecat)