import random
import matplotlib.pyplot as plt
import time

x_val = []
y_val = []

for _ in range(1000):
#     break
    x_val.append(random.random()*10)
    y_val.append(random.random()*10)
    
    color = random.choice(['#008744','#0057e7','#d62d20','#ffa700'])

    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.scatter(x_val,y_val, color=color)
    
    plt.pause(1)
