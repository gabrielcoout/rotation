import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use(['science','notebook','grid'])

x = np.linspace(-10,10,100)
y = x**2

# Define a figura e o eixo
fig, ax = plt.subplots()
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.plot(x,y)
line, = ax.plot(x,y,'red')
text = ax.text(0.1, 0.8, '', fontsize=15,
                    bbox=dict(facecolor='white', edgecolor='black'), 
                    transform=ax.transAxes)


def rotate(X,Y,theta):
    x_0, y_0 = X*np.cos(theta) - Y*np.sin(theta), X*np.sin(theta) + Y*np.cos(theta)
    return x_0 , y_0

def update(frame):
    global x,y
    x_0,y_0 = rotate(x,y,frame)
    line.set_data(x_0,y_0)
    text.set_text(r'$\theta$={:.0f}°'.format(frame/np.pi*180))

# # Cria a animação
ani = FuncAnimation(fig, update, frames=np.arange(0,2*np.pi+0.1,0.1), interval=5)

# Mostra a animação
plt.show()