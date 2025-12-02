import numpy as np

def xavier(node_num):
    return np.random.radn(node_num)/np.sqrt(1.0 /node_num)

def he(node_num)：
    return np.random.radn(node_num)/np.sqrt(2.0 /node_num)