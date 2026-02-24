class Variable:
    def __init__(self,data):
        self.data=data
        self.grad=None  #导数
        self.creators=[] #父类

    def __init__(self,data,weight,value):
        self.data=data
        self.grad=None
        self.creators.append(weight)
        self.creators.append(value)


class Variables:

    def __init__(self,val):
        self.grad=None
        self.creators=[]
        self.creators.append(val)
        for a in val:
             self.data=self.data+a


class Variable_multiply(Variable):

    def __init__(self,w,d):
        self.data=w*d
        self.grad=None
        self.creators_weight=w
        self.creators_variable=d

    def set_grad():
        self.creators_weight.grad=self.creators_variable*self.grad
        self.creators_variable.grad=self.creators_weight*self.grad




class Variable_batch_add(Variable):
    
    def __init__(self,d):
        for val in a:
            self.data+=val.data

        self.grad=None
        self.creators=d

    def set_grad():
        for val in self.creators:
            val.grad=self.grad

    