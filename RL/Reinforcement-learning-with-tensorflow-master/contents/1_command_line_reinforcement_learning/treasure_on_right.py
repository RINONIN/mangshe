"""
A simple example for Reinforcement Learning using table lookup Q-learning method.
An agent "o" is on the left of a 1 dimensional world, the treasure is on the rightmost location.
Run this program and to see how the agent will improve its strategy of finding the treasure.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

import numpy as np
import pandas as pd
import time

np.random.seed(2)  # reproducible
# seed( ) 用于指定随机数生成时所用算法开始的整数值。
# 1.如果使用相同的seed( )值，则每次生成的随即数都相同；
# 2.如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。
# 3.设置的seed()值仅一次有效

N_STATES = 6  # 一维世界的长度
ACTIONS = ['left', 'right']  # 可选择的动作
EPSILON = 0.8  # 贪婪率，80%选择最优
ALPHA = 0.1  # 学习率
GAMMA = 0.9  # 奖励衰减率
MAX_EPISODES = 10  # 最大代数
FRESH_TIME = 0.5  # 执行一个动作的时长


def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),  # q_table 初始化为0 , 建立一个 6*2 的矩阵
        columns=actions,  # 动作名称
        # index=['1', '2', '3', '4', '5', '6']
    )
    # print(table)  # 显示 q_table
    return table


def choose_action(state, q_table):
    # 动作选择
    state_actions = q_table.iloc[state, :]  # 提取指定行列的数据，取所选中的state行所有列的数据
    if (np.random.uniform() > EPSILON) or ((state_actions == 0).all()):  # 随机数大于epsilon，执行非贪婪准则，随机选择动作
        action_name = np.random.choice(ACTIONS)  # 随机选择一个动作
    else:  # 执行贪婪准则
        action_name = state_actions.idxmax()  # 返回取到最大值的索引 默认是列（其中括号中的axis=0是列，axis=1是行）
        # replace argmax to idxmax as argmax means a different function in newer version of pandas
    return action_name  # 返回动作名称


def get_env_feedback(S, A):
    # 环境反馈
    if A == 'right':  # 向右移动
        if S == N_STATES - 2:  # terminate 向右移动至总体长度-2时，则到达终点
            S_ = 'terminal'
            R = 1  # 奖励
        else:
            S_ = S + 1
            R = 0
    else:  # move left
        R = 0
        if S == 0:
            S_ = S  # reach the wall 向左移动至起点时，则到达终点
        else:
            S_ = S - 1
    return S_, R


def update_env(S, episode, step_counter):
    # 环境更新
    env_list = ['-'] * (N_STATES - 1) + ['T']  # '-----T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode + 1, step_counter)
        print('\r{}'.format(interaction), end='')  # 打印当前回合数以及所用步数
        time.sleep(2)  # 推迟执行2秒
        print('\r                                ', end='')
    else:
        env_list[S] = 'λ'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


def rl():
    # 强化学习主循环
    q_table = build_q_table(N_STATES, ACTIONS)
    for episode in range(1, MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminated = False
        update_env(S, episode, step_counter)
        while not is_terminated:

            A = choose_action(S, q_table)  # 采取行动
            S_, R = get_env_feedback(S, A)  # 获取下一步的状态和奖励
            q_predict = q_table.loc[S, A]  # 从q表获取预测值
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max()  # 下一个状态不是终点，选择最大的奖励值
            else:
                q_target = R  # 下一个状态是终点
                is_terminated = True  # 终止该回合

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  # 更新q表
            S = S_  # 移动到下一状态

            update_env(S, episode, step_counter + 1)  # 更新环境
            step_counter += 1
    return q_table


if __name__ == "__main__":
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)
