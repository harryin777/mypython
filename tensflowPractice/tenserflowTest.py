import tensorflow as tf

random_float = tf.random.uniform(shape=())
print(random_float)
print(1111)

# 定义一个有2个元素的零向量
zero_vector = tf.zeros(shape=2)

# 定义两个2×2的常量矩阵
A = tf.constant([[1., 2.], [3., 4.]])
B = tf.constant([[5., 6.], [7., 8.]])

# 查看矩阵A的形状、类型和值
print(A.shape)
print(A.dtype)
print(A.numpy())

# 计算矩阵A和B的和
C = tf.add(A, B)
print(C)
# 计算矩阵A和B的乘积
D = tf.matmul(A, B)
print(D)

# 自动求导机制
# 变量与普通张量的一个重要区别是其默认能够被 TensorFlow 的自动求导机制所求导
x = tf.Variable(initial_value=3.)
with tf.GradientTape() as tape:  # 在 tf.GradientTape() 的上下文内，所有计算步骤都会被记录以用于求导
    y = tf.square(x)
y_grad = tape.gradient(y, x)  # 计算y关于x的导数
print('y 关于 x 的导数')
print(y_grad)
