class Variable
    def __init__(self,data):
        self.data=data
        self.grad=None  #导数
        self.creator=None #父类

    def __init__(self,data,weight):
        self.data=data
        self.grad=None
        self.creator=weight