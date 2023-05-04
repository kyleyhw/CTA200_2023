import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot:
    def __init__(self):
        steps = 10
        self.xmin, self.xmax = (-2, 2)
        self.ymin, self.ymax = (-2, 2)
        self.x = np.linspace(self.xmin, self.xmax, steps)
        self.y = np.linspace(self.ymin, self.ymax, steps)

        x_coord, y_coord = np.meshgrid(self.x, self.y)

        self.complex_plane = np.zeros(shape=(len(x_coord), len(y_coord)), dtype=complex) + x_coord + 1j * y_coord

        self.scale = np.zeros_like(self.complex_plane, dtype=float)

        for i in range(len(self.scale)):
            for j in range(len(self.scale[i])):
                self.scale[i, j] = self.iterate(self.complex_plane[i, j])

    def diverge(self, x):
        if x > 1e+10:
            return True
        return False

    def iterate(self, c, z_0=0, iterations=20):
        z = z_0
        for i in range(iterations):
            z = z**2 + c
            if self.diverge(np.abs(z)):
                return i
        return 0

    def plot_binary(self, show=False):
        plt.figure()
        binary = np.where(self.scale == 0, 0, 1)
        plt.imshow(binary, extent=[self.xmin, self.xmax, self.ymin, self.ymax])
        if show:
            plt.show()

    def plot_scale(self, show=False):
        plt.figure()
        plt.imshow(self.scale, extent=[self.xmin, self.xmax, self.ymin, self.ymax], interpolation='blinear')
        if show:
            plt.show()