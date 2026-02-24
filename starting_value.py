import numpy as np
import pickle
from dataset.mnist import load_mnist

def xavier(node_num1,node_num2,node_num3):
    return np.random.randn(node_num1,node_num2)/np.sqrt(node_num3)

def he(node_num):
    return np.random.randn(node_num)*np.sqrt(2)/np.sqrt(node_num)


def set_value():
    value1=xavier(784,784,784)
    value2=xavier(28,28,784)
    value3=xavier(14,14,28)
    value4=xavier(10,10,14)

    data={'w1':value1,'w2':value2,'w3':value3,'w4':value4}
    
    with open('mnist.pkl','wb') as file
      pickle.dump(data,file)


#数据大小为60000
def import_data():
    (x_train,t_train),(x_test,t_test)=load_mnist(flatten=True,normalize=False)
    random_integers = [random.randint(0, 59999) for _ in range(100)]
    x_1=[]
    t_1=[]
    for a in random_integers:
        x_1.append(x_train[a])
        t_1.append(t_train[a])

    return x_1,t_1
    



