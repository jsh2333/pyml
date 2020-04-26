arr=np.arange(8).reshape(2,4)
arr
# array([[0, 1, 2, 3],
#        [4, 5, 6, 7]]) 


b=arr[0]
b
# array([0, 1, 2, 3])


arr[0]=10
arr
# array([[10, 10, 10, 10],
#        [ 4,  5,  6,  7]])
b
# Out[127]: array([10, 10, 10, 10])

# slicing 복사본 생성
b=arr[0].copy()
b
# array([0, 1, 2, 3])


# def asarray(a, dtype=None, order=None):
#     return array(a, dtype, copy=False, order=order) 

arr = np.ones((3,4))
arr

arrB = np.asarray(arr) # 참조본 생성
arrC = np.array(arr) #복사본 생성
arr[1]=np.pi # 원본 변경
arr
# array([[ 1.        ,  1.        ,  1.        ,  1.        ],
#        [ 3.14159265,  3.14159265,  3.14159265,  3.14159265],
#        [ 1.        ,  1.        ,  1.        ,  1.        ]])
arrB # 참조본은 자동으로 변경된다.
# array([[ 1.        ,  1.        ,  1.        ,  1.        ],
#        [ 3.14159265,  3.14159265,  3.14159265,  3.14159265],
