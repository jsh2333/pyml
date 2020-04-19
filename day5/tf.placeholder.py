import tensorflow as tf    
print(tf.__version__)
#tf.compat.v1.disable_eager_execution()
#tf.disable_v2_behavior()

# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)

a = tf.function(tf.float32)
b = tf.function(tf.float32)


adder_node = a+ b

sess = tf.Session()
out1 = sess.run(adder_node, feed_dict={a:3, b:4.5})
out2 = sess.run(adder_node, feed_dict={a:[1,3], b:[2,4]})
print(out1)
print(out2)