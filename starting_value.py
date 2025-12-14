import numpy as np
import pickle

def xavier(node_num1,node_num2,node_num3):
    return np.random.randn(node_num1,node_num2)/np.sqrt(node_num3)

def he(node_num):
    return np.random.randn(node_num)*np.sqrt(2)/np.sqrt(node_num)


def set_value():
    value1=xavier(784,784,784)
    value2=xavier(28,28,28)
    value3=xavier(14,14,14)
    value4=xavier(10,10,10)

    data=[]
    data.extend(value1)
    data.extend(value2)
    data.extend(value3)
    data.extend(value4)


    with open('mnist.pkl','wb') as file
      pickle.dump(data,file)
