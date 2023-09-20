import simpy
import random
import statistics
import numpy as np

def clock(env, name, tick):
    while True:
        print(name, env.now)
        yield env.timeout(tick)

spheros = np.linspace(1,50,number=50)


env = simpy.Environment()



#print(clock(env,"Alex",1))

