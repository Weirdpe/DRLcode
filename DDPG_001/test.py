from env import Vehicle, RSU, IIov_Env


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
    {'loc_v_x': 2,
     'loc_v_y': 3,
     'speed': 30,
     'compute_freq': 20,
     'queue_size': 100,
     'working_size': 20,
     'cache_size': 30,
     'task': tasks_category}
]

vehicles = []
for i in range(2):
    vehicles.append(Vehicle(
        vecs[i]['loc_v_x'],
        vecs[i]['loc_v_y'],
        vecs[i]['speed'],
        vecs[i]['compute_freq'],
        vecs[i]['queue_size'],
        vecs[i]['working_size'],
        vecs[i]['cache_size'],
        vecs[i]['task'],
    ))

env = IIov_Env(2, 2)
env._generate_vehicles()
print(env.vehicles[1].task)



