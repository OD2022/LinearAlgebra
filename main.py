import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')
plt.figure(figsize=(6, 4))
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

container = []

r = 6 * np.random.random(5000)
theta = 2 * np.pi * np.random.random(5000)
row1 = (r * np.sin(theta))
row2 = (r * np.cos(theta))
row3 = (np.sin(np.sqrt(row1**2 + row2**2)))
row4 = [i for i in range(len(row1))]
default_matrix = np.matrix([row1, row2, row3, row4])
container.append(default_matrix)


class Hat():

  def __init__(self):
    self.matrix = container[0]

  def draw_hat(self):
    x = self.matrix[0]
    y = self.matrix[1]
    z = self.matrix[2]
    return x, y, z

  def xz_reflect_matrix(self):
    trans = np.matrix([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0],
                       [0, 0, 0, 1]])
    self.matrix = trans * self.matrix

  def scale_matrix(self, s, t, u):
    trans = np.matrix([[s, 0, 0, 0], [0, t, 0, 0], [0, 0, u, 0], [0, 0, 0, 1]])
    self.matrix = trans * self.matrix

  def clock_x_rotate_matrix(self, x):
    A = np.matrix([[1, 0, 0, 0], [0, np.cos(x), np.sin(x), 0],
                   [0, np.sin(-x), np.cos(x), 0], [0, 0, 0, 1]])
    self.matrix = A * self.matrix

  def clock_y_rotate_matrix(self, x):
    A = np.matrix([[np.cos(x), 0, np.sin(-x), 0], [0, 1, 1, 0],
                   [np.sin(-x), 0, np.cos(x), 0], [0, 0, 0, 1]])
    self.matrix = A * self.matrix

  #Adding the ones from transformations
  def anticlock_x_rotate_matrix(self, x):
    A = np.matrix([[1, 0, 0, 0], [0, np.cos(x), np.sin(-x), 0],
                   [0, np.sin(x), np.cos(x), 0], [0, 0, 0, 1]])
    self.matrix = A * self.matrix

  def anticlock_y_rotate_matrix(self, x):
    A = np.matrix([[np.cos(x), 0, np.sin(-x), 0], [0, 1, 1, 0],
                   [np.sin(-x), 0, np.cos(x), 0], [0, 0, 0, 1]])
    self.matrix = A * self.matrix

  def anticlock_z_rotate_matrix(self, y):
    A = np.matrix([[np.cos(y), np.sin(-y), 0, 0], [np.sin(y),
                                                   np.cos(y), 0, 0],
                   [0, 0, 1, 0], [0, 0, 0, 1]])
    self.matrix = A * self.matrix

  def perspective_matrix(self, d):
    A = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0],
                   [0, 0, (-1 / d), 1]])
    self.matrix = A * self.matrix

  def x_shear_matrix(self, s):
    A = np.matrix([[1, s, s, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    self.matrix = A * self.matrix

  def y_shear_matrix(self, s):
    A = np.matrix([[1, 0, 0, 0], [s, 1, s, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    self.matrix = A * self.matrix

  def z_shear_matrix(self, s):
    A = np.matrix([[1, 0, 0, 0], [s, 1, s, 0], [s, s, 0, 0], [0, 0, 0, 1]])
    self.matrix = A * self.matrix

  def translate_matrix(self, x, y, z):
    A = np.matrix([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]])
    self.matrix = A * self.matrix

  def xy_reflect_matrix(self):
    A = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    self.matrix = A * self.matrix

  def yz_reflect_matrix(self):
    A = np.matrix([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    self.matrix = A * self.matrix


def xz_reflect_matrix(self):
  A = np.matrix([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
  self.matrix = A * self.matrix
