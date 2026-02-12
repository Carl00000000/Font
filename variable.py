class Variable
    def __init__(self,data):
        self.data=data
        self.grad=None  #导数
        self.creators=[] #父类

    def __init__(self,data,weight,value):
        self.data=data
        self.grad=None
        self.creators.append(weight)
        self.creators.append(value)


class Variables

    def __init__(self,val):
        self.grad=None
        self.creators=[]
        self.creators.append(val)
        for a in val:
             self.data=self.data+a