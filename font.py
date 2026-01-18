import sys,os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
import starting_value
import pickle

def img_show(img):
  pil_img=Image.fromarray(np.uint8(img))
  pil_img.show()

(x_train,t_train),(x_test,t_test)=load_mnist(flatten=True,normalize=False)
img=x_train[0]
label=t_train[0]
print(label)
print(img[10])
#img=img.reshape(28,28)
#img_show(img)
#图片展示

def get_weight():
  file_path='mnist.pkl'
  if os.path.exists(file_path):
    with open('mnist.pkl','rb') as file:
      loaded_data=pickle.load(file)
  else:
    starting_value.set_value()
    with open('mnist.pkl','rb') as file:
      loaded_data=pickle.load(file)
  return loaded_data
    




# MINIST数据集28X28 1
#设定权重为(28,14,10)

class Font:
    
    def __init__(self,):
        (x_train,t_train),(x_test,t_test)=load_mnist(flatten=True,normalize=False)
        self.parmas={}
        weight=get_weight()
        '''
        i=0
        value=[]
        while i<784:
          value.extend(weight[i])
          i+=1
        self.parmas['W1']=value
        value=[]
        while i<28:
          value.extend(weight[i+784])
          i+=1
        self.parmas['W2']=value
        value=[]
        while i<14:
          value.extend(weight[i+812])
          i+=1
        self.parmas['W3']=value
        value=[]
        while i<10:
          value.extend(weight[i+826])
          i+=1
        self.parmas['W4']=value
        '''
        self.parmas['w1']=weight['w1']
        self.parmas['w2']=weight['w2']
        self.parmas['w3']=weight['w3']
        self.parmas['w4']=weight['w4']


        get_input=

        for i in get_input:
          predict(i)






    
    def predict(self,x):
        w1,w2,w3,w4=self.parmas['w1'],self.parmas['w2'],self.parmas['w3'],self.parmas['w4']

        a1=np.dot(x,w1)+b1

        a2=