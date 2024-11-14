import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #오버플로 대첵
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y


a1 = np.array([0.3, 2.9, 4.0])
y1 = softmax(a1)
print(y1)

sum_y1 = np.sum(y1)
print(sum_y1) # 소프트 맥스의 총합은 1