import tensorflow as tf
# TF 2.0 supports eager execution 
# which means 
# you don't have to explicitly create a session and run the code in it. 
# So the simplest solution would be:
# https://stackoverflow.com/questions/57206247/how-to-fix-runtimeerror-the-session-graph-is-empty-add-operations-to-the-grap
print(tf.__version__)

# 상수 정의 --- (※2)
a = tf.constant(1234)
b = tf.constant(5000)
# 계산 정의 --- (※3)
add_op = a + b

# 세션 시작하기 --- (※4)
# sess = tf.Session()
# sess= tf.compat.v1.Session()

#res = sess.run(add_op) # 식 평가하기
print(add_op)
