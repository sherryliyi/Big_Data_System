import tensorflow as tf

image_decoded = tf.image.decode_jpeg(tf.read_file('cat.0.jpg'), channels=3)
# cropped = tf.image.resize_image_with_crop_or_pad(image_decoded, 64, 64)
cropped = tf.image.resize_images(image_decoded, size=[128,128], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
enc = tf.image.encode_jpeg(cropped)
fname = tf.constant('cat_0_128.jpg')
fwrite = tf.write_file(fname, enc)

sess = tf.Session()
result = sess.run(fwrite)