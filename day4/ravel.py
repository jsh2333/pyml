

import numpy as np

x = np.arange(12).reshape(3,4)

x

y = np.ravel(x, order='C') # default:  C와 같은 순서로 인덱싱하여 평평하게 배열
y

y = np.ravel(x, order='F') # fortran와 같은 순서로 인덱싱하여 평평하게 배열
y

y = np.ravel(x, order='K') # 메모리 발생 순서로 인덱싱하여 평평하게 배열
y


x = np.arange(12).reshape(2, 3, 2)
x

y = np.ravel(x, order='C')
y

x = np.arange(12).reshape(2, 3, 2).swapaxes(1, 2)
x

y = np.ravel(x, order='K')


