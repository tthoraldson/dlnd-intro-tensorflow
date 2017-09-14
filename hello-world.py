import tensorflow as tf


def run():
    output = None
    x = tf.placeholder(tf.string)

    with tf.Session() as sess:
        # TODO: Feed the x tensor 123
        output = sess.run(x, feed_dict={x: "Hello, world!"})

    print(output)
    return output

run()
