# Solution is available in the other "solution.py" tab
import tensorflow as tf


def run():
    output = None
    logit_data = [2.0, 1.0, 0.1]
    logits = tf.placeholder(tf.float32)

    # TODO: Calculate the softmax of the logits
    softmax = tf.nn.softmax(logit_data)

    with tf.Session() as sess:
        # TODO: Feed in the logit data
        output = sess.run(softmax)

    return output
