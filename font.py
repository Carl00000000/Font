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

file_path='mnist.pkl'
if os.path.exists(file_path):

else:
  starting_value.set_value()


# MINIST数据集28X28 1
#设定权重为(28,14,10)

class Font:
    
    def __init__(self,):
        (x_train,t_train),(x_test,t_test)=load_mnist(flatten=True,normalize=False)
        self.parmas={}
        self.parmas['W1']=starting_value.xavier(28)
        self.parmas['W2']=starting_value.xavier(28)

    
    def predict(self,x):
        w1,w2=self.parmas['W1'],self.parmas['W2']
        b1,b2=self.parmas['b1'],self.parmas['b2']

        a1=np.dot(x,w1)+b1

        a2=