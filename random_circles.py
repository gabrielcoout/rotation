import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from circle_obj import circle

c_0 = circle(radius=1, center=(5,5))
c_1 = circle(radius=3, center=(5,5))
c_2 = circle(radius=5, center=(5,5))


# Define a figura e o eixo
fig, ax = plt.subplots(1,2, gridspec_kw={'width_ratios': [3, 1]}, figsize=(8,5))
ax[1].set_axis_off()
ax[0].set_xlim(0, 10)
ax[0].set_ylim(0, 10)
ax[0].plot(c_0.x,c_0.y,color ='black')
ax[0].plot(c_1.x,c_1.y,color ='black')
ax[0].plot(c_2.x,c_2.y,color ='black')

time_text = ax[1].text(-0.1, 0.95, '', fontsize=15,
                    bbox=dict(facecolor='white', edgecolor='black'), 
                    transform=ax[1].transAxes)
text1 = ax[1].text(-0.1, 0.65, '', fontsize=15,
                    bbox=dict(facecolor='white', edgecolor='black'), 
                    transform=ax[1].transAxes)
text2 = ax[1].text(-0.1, 0.35, '', fontsize=15,
                    bbox=dict(facecolor='white', edgecolor='black'), 
                    transform=ax[1].transAxes)

# Define as quatro cores
colors = ['#008744','#0057e7','#d62d20','#ffa700']
n0 = np.zeros(4) 

# Função para mapear as coordenadas x e y em uma cor
def get_color(x, y):
    if c_0.is_inside(x,y):
        return colors[3]
    elif c_1.is_inside(x,y):
        return colors[2]
    elif c_2.is_inside(x,y):
        return colors[1]
    else:
        return colors[0]
    
def decide(color):
    if color == colors[0]:
        n0[0]=n0[0]+1
    elif color == colors[1]:
        n0[1]=n0[1]+1
    elif color == colors[2]:
        n0[2]=n0[2]+1
    if color == colors[3]:
        n0[3]=n0[3]+1
    

# Função para gerar os pontos aleatórios
def generate_points():
    x = random.random()*10
    y = random.random()*10
    return x, y

# Função para atualizar os pontos e as cores em cada quadro
def update(frame):
    x, y = generate_points()
    color = get_color(x, y)
    # color_count(color)
    ax[0].scatter(x, y, color=color)
    time_text.set_text('t={:.2f}'.format(frame/60))
    decide(color)
    text1.set_text(f'yellow={n0[3]}\nred={n0[2]}\nblue={n0[1]}\ngreen={n0[0]}')
    text2.set_text(f'yellow={n0[3]/n0.sum():.2f}\nred={n0[2]/n0.sum():.2f}\nblue={n0[1]/n0.sum():.2f}\ngreen={n0[0]/n0.sum():.2f}')

    

# Cria a animação
# interval - time between frames in miliseconds
# frames - iterable
ani = FuncAnimation(fig, update, frames=range(60), interval=100)

# Mostra a animação
plt.show()