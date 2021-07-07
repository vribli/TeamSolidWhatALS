import matplotlib.pyplot as plt
from scipy import signal

# assume [0, 100] -> [0, 100]

class BrightnessTable:
    def __init__(self, x=[0, 100], y=[0, 100]):
        self.x = x
        self.y = y
        gradient = (self.y[1] - self.y[0]) / (self.x[1] - self.x[0])
        self.table = {i : int(gradient * i + self.y[0]) for i in range(self.x[0], self.x[1] + 1)}
        xs = list(range(self.x[0], self.x[1] + 1))
        ys = [self.get_brightness(x) for x in xs]
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.lines, = self.ax.plot(xs, ys)
        self.ax.set(xlabel='Environmental brightness', ylabel='Screen brightness')
        self.ax.grid()
        	
        # TODO: update based on curves online -- can be logarithmic??

    def get_brightness(self, x):
        result = self.table[x]
        if result < self.x[0]:
            return self.x[0]
        elif result > self.x[1]:
            return self.x[1]
        else:
            return result
    
    # Gaussian decay to update
    def update(self, x, y, lr=0.7, radius=50, std=12, enforce=True):
        decay = signal.gaussian(2 * radius + 1, std)
        diff = self.table[x] - y
        for i, j in enumerate(range(x - radius, x + radius + 1)):
            if self.x[0] <= j <= self.x[1]:
                self.table[j] -= diff * lr * decay[i]
        if enforce == True:
            self.enforce_monotonic()
        
    def plot(self):
        xs = list(range(self.x[0], self.x[1] + 1))
        ys = [self.get_brightness(x) for x in xs]
        self.lines.set_xdata(xs)
        self.lines.set_ydata(ys)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events() 

    def reset(self):
        gradient = (self.y[1] - self.y[0]) / (self.x[1] - self.x[0])
        self.table = {i : int(gradient * i + self.y[0]) for i in range(self.x[0], self.x[1] + 1)}

    def enforce_monotonic(self):
        for i in range(self.x[1] - self.x[0]):
            if self.table[i] > self.table[i + 1]:
                self.table[i + 1] = self.table[i]
