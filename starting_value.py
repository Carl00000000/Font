import numpy as np

def xavier(node_num):
    return np.random.radn(node_num)/np.sqrt(node_num)

def he(node_num)：
    return np.random.radn(node_num)*np.sqrt(2)/np.sqrt(node_num)