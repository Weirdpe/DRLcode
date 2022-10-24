import scipy.io as sio
import numpy as np

import math as mh

"""
奖励函数
"""

"""
计算时延：
任务量/计算频率；  任务量=系数c * 任务数据大小

传输时延：
任务数据大小/传输速率

等待时间

汽车移动模型

能耗模型

存储容量

定义RSU的位置：Average RSU's transmission range:600m
Inter-RSU distance(D):2-6km
Vehicle density: 0.003 - 0.007vehicle/m
"""
"""
状态空间设计：
任务大小 计算资源大小 最大容忍时延 平均队列剩余空间大小  
"""

"""
车辆类：
位置信息：loc_v_x, loc_v_y
速度:speed
CPU频率:compute_v_freq
队列大小:queue_v_size
计算中的队列大小:working_v_size
等待队列大小：cache_v_size
剩余队列大小 = queue_v_size - working_v_size - cache_v_size
"""


class Vehicle(object):
    def __init__(self, loc_v_x, loc_v_y, speed, compute_freq, queue_size, working_size, cache_size, task):
        self.loc_v_x = loc_v_x
        self.loc_v_y = loc_v_y
        self.speed = speed
        self.compute_freq = compute_freq
        self.queue_size = queue_size
        self.working_size = working_size
        self.cache_size = cache_size
        self.task = task  # 字典列表保存任务

    # 判断在哪个RSU的范围内
    """
    任务： 
    任务大小 task_size
    需要多少周期 amountFreq
    容忍时间 max_latency
    任务优先级 task_prior 
    哪个时隙产生的：step_index
    是否做完:is_done
    """


tasks_category = [
    {
        'task_size': 20,
        'amount_freq': 30,
        'max_latency': 0.2,
        'task_prior': 3,
        'step_index': 2,
        'is_done': False},
    {
        'task_size': 30,
        'amount_freq': 20,
        'max_latency': 0.4,
        'task_prior': 2,
        'step_index': 4,
        'is_done': False},
    {
        'task_size': 40,
        'amount_freq': 40,
        'max_latency': 0.3,
        'task_prior': 1,
        'step_index': 3,
        'is_done': False}
]

vecs = [
    {
        'loc_v_x': 1,
        'loc_v_y': 1,
        'speed': 20,
        'compute_freq': 20,
        'queue_size': 100,
        'working_size': 20,
        'cache_size': 30,
        'task': tasks_category},
    {
        'loc_v_x': 2,
        'loc_v_y': 3,
        'speed': 30,
        'compute_freq': 20,
        'queue_size': 100,
        'working_size': 20,
        'cache_size': 30,
        'task': tasks_category}
]
v_range_rsu = []  # 判断车辆属于哪个RSU

"""
有m种任务，车辆每次从这些任务中随机抽取k个，可以重复。

"""

vehicle1 = Vehicle(1, 2, 20, 30, 100, 50, 60, tasks_category)

"""
RSU类：
位置信息：loc_r_x, loc_r_y
CPU频率：compute_r_freq
队列大小：queue_r_size
计算中的队列大小:working_r_size
等待队列大小：cache_r_size
剩余队列大小: = queue_r_size - working_r_size - cache_r_size
"""


class RSU(object):
    def __init__(self, loc_r_x, loc_r_y, compute_r_freq, working_r_size, cache_r_size):
        self.loc_r_x = loc_r_x
        self.loc_r_y = loc_r_y
        self.compute_r_freq = compute_r_freq
        self.working_r_size = working_r_size
        self.cache_r_size = cache_r_size


class IIov_Env(object):
    def __init__(self, vehicle_number, rsu_number):
        self.vehicle_number = vehicle_number
        self.rsu_number = rsu_number
        self.vehicles = []

    def _generate_vehicles(self) -> None:
        for vehicle_i in range(self.vehicle_number):
            self.vehicles.append(Vehicle(
                vecs[vehicle_i]['loc_v_x'],
                vecs[vehicle_i]['loc_v_y'],
                vecs[vehicle_i]['speed'],
                vecs[vehicle_i]['compute_freq'],
                vecs[vehicle_i]['queue_size'],
                vecs[vehicle_i]['working_size'],
                vecs[vehicle_i]['cache_size'],
                vecs[vehicle_i]['task']
            ))

    def step(self):
        pass

    def reward(self):
        pass


env = IIov_Env(2, 2)
env._generate_vehicles()
print(env.vehicles[1].task[1]['task_size'])

"""
判断是否在某一个RSU的通信范围内
将每个RSU的位置与车辆的位置计算距离，如果小于通信半径的话，则表示在范围之内。
m个RSU n辆车
"""

"""
判断V2V的通信范围内有哪些车
"""
n = 7  # 车辆数量
m = 8  # RSU数量
"""
距离数组
"""
Dis_RSU = np.zeros((n, n), dtype=float)

IIR_RSU = np.zeros((n, n), dtype=float)

"""
判断车辆i可以卸载到哪个RSU
"""

IIR_Vehicle = np.zeros((n, m), dtype=float)

"""

"""
RSU_loc = []  # 由m个二维坐标表示
V_loc = []

"""
任务生成
"""


def isinrange_rsu(rsu_loc, v_loc):
    for i in range(rsu_loc):
        pass


def isinrange_vehicle():
    pass
