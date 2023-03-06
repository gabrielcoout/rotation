from numpy import array, arange, pi, cos, sin

class circle:
    def __init__(self,radius,theta=arange(0,2*pi+0.1,0.1),center=(0,0)):
        self.radius = radius 
        self.angle = theta
        self.center = center
        self.x = cos(self.angle)*self.radius+self.center[0]
        self.y = sin(self.angle)*self.radius+self.center[1]
    
    def __repr__(self):
        return f'center: {self.center}, radius = {self.radius}'

    def is_inside(self , x , y):
        return (x-self.center[0])**2+(y-self.center[1])**2 <= self.radius**2
        
    

if __name__ == '__main__':
    c = circle(radius=1)
    print(c.is_inside(1,0))
    