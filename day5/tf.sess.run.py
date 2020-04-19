import tensorflow as tf
g1 = tf.Graph()
with g1.as_default() as graph:
    n1 = tf.constant(3) # g1에 n1 노드 생성 추가

sess = tf.Session() # graph 명시하지 않으면 default graph사용
sess.run(n1)
sess1=tf.Session(graph=g1)
sess1.run(n1)