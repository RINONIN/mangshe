"""
This part of code is the Q learning brain, which is a brain of the agent.
All decisions are made in here.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

import numpy as np
import pandas as pd


class QLearningTable:
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions  # a list
        self.lr = learning_rate  # 学习率
        self.gamma = reward_decay  # 奖励衰减
        self.epsilon = e_greedy  # 贪婪参数
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)  # q表

    def choose_action(self, observation):  # 动作选择
        self.check_state_exist(observation)  # 检查更新
        # 动作选择
        if np.random.uniform() < self.epsilon:
            # 选择最佳动作
            state_action = self.q_table.loc[observation, :]
            # 某些选择的值可能相同，因此随机进行选择
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        else:
            # 随机选择动作
            action = np.random.choice(self.actions)
        return action

    def learn(self, s, a, r, s_):  # 学习过程
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]  # q预测值
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()  # next state is not terminal
        else:
            q_target = r  # next state is terminal
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  # update

    def check_state_exist(self, state):  # 检查当前状态
        if state not in self.q_table.index:
            # 当前状态不在Q表中，则为q表增加一个新的状态
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )
