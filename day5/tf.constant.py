import tensorflow as tf

const1 = tf.constant(3.0, tf.float32)
#const1 = tf.constant(3.0)
const2 = tf.constant(4.0)
const_add = tf.add(const1, const2)

print("n1: ", const1, "\nn2: ", const2 )
print("add: ", const_add)

# tf.compat.v1.disable_eager_execution()
# # tf.executing_eagerly()

print(tf.__version__)
# sess = tf.compat.v1.Session()
  #sess=tf.Session()
#print("sess.run(n1, n2): ", sess.run(const1, const2))
#print("sess.run(add): ", sess.run(const1, const2))
print("sess.run(add): ", const_add)


