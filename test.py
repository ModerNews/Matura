import time
from everydayAPI import *

list = list_generator(1000000, 5)

start_time = time.time()
print(f"Official: Leader is {array_leader_cross(list)}, execution took {time.time() - start_time}")

start_time = time.time()
print(f"Grzegorz: Leader is {array_leader(list)}, execution took {time.time() - start_time}")

start_time = time.time()
print(f"Rafał: Leader is {array_leader_count(list)}, execution took {time.time() - start_time}")

start_time = time.time()
print(f"Rafał, set: Leader is {set_leader_count(list)}, execution took {time.time() - start_time}")
