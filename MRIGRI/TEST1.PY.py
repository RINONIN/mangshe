"""
作者：RINO
日期: 2021年12月23日
时间: 22:39
"""
import numpy as np

edges = [
    ('Arad', 'Zerind', 75),
    ('Arad', 'Sibiu', 140),
    ('Arad', 'Timisoara', 118),
    ('Zerind', 'Oradea', 71),
    ('Oradea', 'Sibiu', 151),
    ('Timisoara', 'Lugoj', 111),
    ('Lugoj', 'Mehadia', 70),
    ('Mehadia', 'Drobeta', 75),
    ('Drobeta', 'Craiova', 120),
    ('Sibiu', 'Fagaras', 99),
    ('Sibiu', 'Rimnicu Vilcea', 80),
    ('Rimnicu Vilcea', 'Craiova', 146),
    ('Fagaras', 'Bucharest', 211),
    ('Rimnicu Vilcea', 'Pitesti', 97),
    ('Pitesti', 'Bucharest', 101),
    ('Bucharest', 'Giurgiu', 90),
    ('Bucharest', 'Urziceni', 85),
    ('Urziceni', 'Hirsova', 98),
    ('Urziceni', 'Vaslui', 142),
    ('Hirsova', 'Eforie', 86),
    ('Vaslui', 'Iasi', 92),
    ('Iasi', 'Neamt', 87),
]

straight_line = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374,
}

start = 'Arad'
end = 'Bucharest'

path = []  # 存储最优路线
path.append(start)
distance = []  # 存储最优路线的路线长度

for i in range(20):
    path1 = []  # path1中存储该节点的连接城市
    distance1 = []  # distance1中存储该节点连接城市的距离
    for a in range(len(edges)):
        if edges[a][0] == path[-1]:
            path1.append(edges[a][1])
            distance1.append(edges[a][-1])
    # 贪婪最优搜索
    min_distance = 1000
    for b in range(len(path1)):
        if straight_line[path1[b]] < min_distance:
            min_distance = straight_line[path1[b]]
            temp_distance = distance1[b]
            temp_path = path1[b]

    path.append(temp_path)
    distance.append(temp_distance)

    if temp_path == end:
        break

X = ' ——> '.join(path)
Y = np.sum(distance)
print('贪婪搜索_最优路线为:', X)
print('贪婪搜索_最优路线长度为:', Y)
