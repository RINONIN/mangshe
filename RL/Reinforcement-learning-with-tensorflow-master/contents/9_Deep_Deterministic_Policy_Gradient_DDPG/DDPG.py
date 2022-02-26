"""
Deep Deterministic Policy Gradient (DDPG), Reinforcement Learning.
DDPG is Actor Critic based algorithm.
Pendulum example.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/

Using:
tensorflow 1.0
gym 0.8.0
"""

import tensorflow as tf
import numpy as np
import gym
import time

tf.compat.v1.disable_eager_execution()

np.random.seed(1)
tf.compat.v1.set_random_seed(1)

# hyper parameters

MAX_EPISODES = 200
MAX_EP_STEPS = 200
LR_A = 0.001  # learning rate for actor
LR_C = 0.001  # learning rate for critic
GAMMA = 0.9  # reward discount
REPLACEMENT = [
    dict(name='soft', tau=0.01),
    dict(name='hard', rep_iter_a=600, rep_iter_c=500)
][0]  # you can try different target replacement strategies
MEMORY_CAPACITY = 10000
BATCH_SIZE = 32

RENDER = False
OUTPUT_GRAPH = True
ENV_NAME = 'Pendulum-v1'


# Actor


class Actor(object):
    def __init__(self, sess, action_dim, action_bound, learning_rate, replacement):
        self.sess = sess
        self.a_dim = action_dim
        self.action_bound = action_bound
        self.lr = learning_rate
        self.replacement = replacement
        self.t_replace_counter = 0

        with tf.compat.v1.compat.v1.variable_scope('Actor'):
            # input s, output a # 这个网络用于及时更新参数
            self.a = self._build_net(S, scope='eval_net', trainable=True)
            # 这个网络不及时更新参数, 用于预测 Critic 的 Q_target 中的 action
            # input s_, output a, get a_ for critic
            self.a_ = self._build_net(S_, scope='target_net', trainable=False)

        self.e_params = tf.compat.v1.compat.v1.get_collection(tf.compat.v1.compat.v1.GraphKeys.GLOBAL_VARIABLES, scope='Actor/eval_net')
        self.t_params = tf.compat.v1.compat.v1.get_collection(tf.compat.v1.compat.v1.GraphKeys.GLOBAL_VARIABLES, scope='Actor/target_net')

        if self.replacement['name'] == 'hard':
            self.t_replace_counter = 0
            self.hard_replace = [tf.compat.v1.compat.v1.assign(t, e) for t, e in zip(self.t_params, self.e_params)]
        else:
            self.soft_replace = [
                tf.compat.v1.compat.v1.assign(t, (1 - self.replacement['tau']) * t + self.replacement['tau'] * e)
                for t, e in zip(self.t_params, self.e_params)]

    def _build_net(self, s, scope, trainable):
        with tf.compat.v1.compat.v1.variable_scope(scope):
            init_w = tf.compat.v1.random_normal_initializer(0., 0.3)
            init_b = tf.compat.v1.constant_initializer(0.1)
            net = tf.compat.v1.compat.v1.layers.dense(s, 30, activation=tf.compat.v1.nn.relu,
                                                      kernel_initializer=init_w, bias_initializer=init_b, name='l1',
                                                      trainable=trainable)
            with tf.compat.v1.compat.v1.variable_scope('a'):
                actions = tf.compat.v1.compat.v1.layers.dense(net, self.a_dim, activation=tf.compat.v1.nn.tanh,
                                                              kernel_initializer=init_w,
                                                              bias_initializer=init_b, name='a', trainable=trainable)
                scaled_a = tf.compat.v1.multiply(actions, self.action_bound,
                                                 name='scaled_a')  # Scale output to -action_bound to action_bound
        return scaled_a

    def learn(self, s):  # batch update
        self.sess.run(self.train_op, feed_dict={S: s})

        if self.replacement['name'] == 'soft':
            self.sess.run(self.soft_replace)
        else:
            if self.t_replace_counter % self.replacement['rep_iter_a'] == 0:
                self.sess.run(self.hard_replace)
            self.t_replace_counter += 1

    def choose_action(self, s):
        s = s[np.newaxis, :]  # single state
        return self.sess.run(self.a, feed_dict={S: s})[0]  # single action

    def add_grad_to_graph(self, a_grads):
        with tf.compat.v1.compat.v1.variable_scope('policy_grads'):
            # 这是在计算 (dQ/da) * (da/dparams)
            # ys = policy;
            # xs = policy's parameters;
            # a_grads = the gradients of the policy to get more Q
            # tf.compat.v1.gradients will calculate dys/dxs with a initial gradients for ys, so this is dq/da * da/dparams
            self.policy_grads = tf.compat.v1.gradients(
                ys=self.a, xs=self.e_params,  # 计算 ys 对于 xs 的梯度
                grad_ys=a_grads)  # 这是从 Critic 来的 dQ/da

        with tf.compat.v1.compat.v1.variable_scope('A_train'):
            opt = tf.compat.v1.compat.v1.train.AdamOptimizer(-self.lr)  # 负的学习率为了使我们计算的梯度往上升, 和 Policy Gradient 中的方式一个性质
            self.train_op = opt.apply_gradients(zip(self.policy_grads, self.e_params))  # 对 eval_net 的参数更新


#  Critic

class Critic(object):
    def __init__(self, sess, state_dim, action_dim, learning_rate, gamma, replacement, a, a_):
        self.sess = sess
        self.s_dim = state_dim
        self.a_dim = action_dim
        self.lr = learning_rate
        self.gamma = gamma
        self.replacement = replacement

        with tf.compat.v1.compat.v1.variable_scope('Critic'):
            # Input (s, a), output q   # 这个网络是用于及时更新参数
            self.a = tf.compat.v1.stop_gradient(a)  # stop critic update flows to actor
            # 这个 a 是来自 Actor 的, 但是 self.a 在更新 Critic 的时候是之前选择的 a 而不是来自 Actor 的 a.
            self.q = self._build_net(S, self.a, 'eval_net', trainable=True)
            # 这个网络不及时更新参数, 用于给出 Actor 更新参数时的 Gradient ascent 强度
            # Input (s_, a_), output q_ for q_target
            self.q_ = self._build_net(S_, a_, 'target_net',
                                      trainable=False)  # target_q is based on a_ from Actor's target_net

            self.e_params = tf.compat.v1.compat.v1.get_collection(tf.compat.v1.compat.v1.GraphKeys.GLOBAL_VARIABLES, scope='Critic/eval_net')
            self.t_params = tf.compat.v1.compat.v1.get_collection(tf.compat.v1.compat.v1.GraphKeys.GLOBAL_VARIABLES, scope='Critic/target_net')

        with tf.compat.v1.compat.v1.variable_scope('target_q'):  # self.q_ 根据 Actor 的 target_net 来的
            self.target_q = R + self.gamma * self.q_
        # 计算误差并反向传递误差
        with tf.compat.v1.compat.v1.variable_scope('TD_error'):
            self.loss = tf.compat.v1.reduce_mean(
                tf.compat.v1.compat.v1.squared_difference(self.target_q, self.q))  # self.q 又基于 Actor 的 target_net

        with tf.compat.v1.compat.v1.variable_scope('C_train'):
            self.train_op = tf.compat.v1.compat.v1.train.AdamOptimizer(self.lr).minimize(self.loss)

        with tf.compat.v1.compat.v1.variable_scope('a_grad'):
            self.a_grads = tf.compat.v1.gradients(self.q, self.a)[0]  # tensor of gradients of each sample (None, a_dim)

        if self.replacement['name'] == 'hard':
            self.t_replace_counter = 0
            self.hard_replacement = [tf.compat.v1.compat.v1.assign(t, e) for t, e in zip(self.t_params, self.e_params)]
        else:
            self.soft_replacement = [
                tf.compat.v1.compat.v1.assign(t, (1 - self.replacement['tau']) * t + self.replacement['tau'] * e)
                for t, e in zip(self.t_params, self.e_params)]

    def _build_net(self, s, a, scope, trainable):
        with tf.compat.v1.compat.v1.variable_scope(scope):
            init_w = tf.compat.v1.random_normal_initializer(0., 0.1)
            init_b = tf.compat.v1.constant_initializer(0.1)

            with tf.compat.v1.compat.v1.variable_scope('l1'):
                n_l1 = 30
                w1_s = tf.compat.v1.compat.v1.get_variable('w1_s', [self.s_dim, n_l1], initializer=init_w,
                                                           trainable=trainable)
                w1_a = tf.compat.v1.compat.v1.get_variable('w1_a', [self.a_dim, n_l1], initializer=init_w,
                                                           trainable=trainable)
                b1 = tf.compat.v1.compat.v1.get_variable('b1', [1, n_l1], initializer=init_b, trainable=trainable)
                net = tf.compat.v1.nn.relu(tf.compat.v1.matmul(s, w1_s) + tf.compat.v1.matmul(a, w1_a) + b1)

            with tf.compat.v1.compat.v1.variable_scope('q'):
                q = tf.compat.v1.compat.v1.layers.dense(net, 1, kernel_initializer=init_w, bias_initializer=init_b,
                                                        trainable=trainable)  # Q(s,a)
        return q

    def learn(self, s, a, r, s_):
        self.sess.run(self.train_op, feed_dict={S: s, self.a: a, R: r, S_: s_})
        if self.replacement['name'] == 'soft':
            self.sess.run(self.soft_replacement)
        else:
            if self.t_replace_counter % self.replacement['rep_iter_c'] == 0:
                self.sess.run(self.hard_replacement)
            self.t_replace_counter += 1


#  Memory

class Memory(object):
    def __init__(self, capacity, dims):
        self.capacity = capacity
        self.data = np.zeros((capacity, dims))
        self.pointer = 0

    def store_transition(self, s, a, r, s_):
        transition = np.hstack((s, a, [r], s_))
        index = self.pointer % self.capacity  # replace the old memory with new memory
        self.data[index, :] = transition
        self.pointer += 1

    def sample(self, n):
        assert self.pointer >= self.capacity, 'Memory has not been fulfilled'
        indices = np.random.choice(self.capacity, size=n)
        return self.data[indices, :]


env = gym.make(ENV_NAME)
env = env.unwrapped
env.seed(1)

state_dim = env.observation_space.shape[0]
action_dim = env.action_space.shape[0]
action_bound = env.action_space.high

# all placeholder for tf
with tf.compat.v1.name_scope('S'):
    S = tf.compat.v1.compat.v1.placeholder(tf.compat.v1.float32, shape=[None, state_dim], name='s')
with tf.compat.v1.name_scope('R'):
    R = tf.compat.v1.compat.v1.placeholder(tf.compat.v1.float32, [None, 1], name='r')
with tf.compat.v1.name_scope('S_'):
    S_ = tf.compat.v1.compat.v1.placeholder(tf.compat.v1.float32, shape=[None, state_dim], name='s_')

sess = tf.compat.v1.compat.v1.Session()

# Create actor and critic.
# They are actually connected to each other, details can be seen in tensorboard or in this picture:
actor = Actor(sess, action_dim, action_bound, LR_A, REPLACEMENT)
critic = Critic(sess, state_dim, action_dim, LR_C, GAMMA, REPLACEMENT, actor.a,
                actor.a_)  # 将 actor 同它的 eval_net/target_net 产生的 a/a_ 传给 Critic
actor.add_grad_to_graph(critic.a_grads)  # 将 critic 产出的 dQ/da 加入到 Actor 的 Graph 中去

sess.run(tf.compat.v1.compat.v1.global_variables_initializer())

M = Memory(MEMORY_CAPACITY, dims=2 * state_dim + action_dim + 1)

if OUTPUT_GRAPH:
    tf.compat.v1.compat.v1.summary.FileWriter("logs/", sess.graph)

var = 3  # control exploration

t1 = time.time()
for i in range(MAX_EPISODES):
    s = env.reset()
    ep_reward = 0

    for j in range(MAX_EP_STEPS):

        if RENDER:
            env.render()

        # Add exploration noise
        a = actor.choose_action(s)
        a = np.clip(np.random.normal(a, var), -2, 2)  # add randomness to action selection for exploration
        s_, r, done, info = env.step(a)

        M.store_transition(s, a, r / 10, s_)

        if M.pointer > MEMORY_CAPACITY:
            var *= .9995  # decay the action randomness
            b_M = M.sample(BATCH_SIZE)
            b_s = b_M[:, :state_dim]
            b_a = b_M[:, state_dim: state_dim + action_dim]
            b_r = b_M[:, -state_dim - 1: -state_dim]
            b_s_ = b_M[:, -state_dim:]

            critic.learn(b_s, b_a, b_r, b_s_)
            actor.learn(b_s)

        s = s_
        ep_reward += r

        if j == MAX_EP_STEPS - 1:
            print('Episode:', i, ' Reward: %i' % int(ep_reward), 'Explore: %.2f' % var, )
            if ep_reward > -300:
                RENDER = True
            break

print('Running time: ', time.time() - t1)
