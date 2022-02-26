"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hell        [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from maze_env import Maze
from RL_brain import QLearningTable


def update():
    for episode in range(100):  # 共一百回合
        # initial observation
        observation = env.reset()

        while True:
            # 更新环境
            env.render()

            # RL 基于观测值做出动作选择
            action = RL.choose_action(str(observation))

            # RL 采取动作并获得下一步观测值和奖励
            observation_, reward, done = env.step(action)

            # RL 从该回合学习 (s, a, r, s_,) ==> Q_learning
            RL.learn(str(observation), action, reward, str(observation_))

            # 替换观测值
            observation = observation_

            # 回合结束退出循环
            if done:
                break

    # end of game
    print('game over')
    env.destroy()


if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
