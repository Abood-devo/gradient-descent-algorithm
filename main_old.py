#https://medium.com/@ilmunabid/how-to-find-a-gradient-slope-of-a-function-in-python-774f865467d2
import random

import matplotlib.pyplot as mpl
import numpy as np
import sympy

step = 1
x_axe = np.arange(0, 30.1, step/10)
loss_function = list(0.1 * (x-19)**2 + 1 for x in x_axe)
loss_function_grad = np.gradient(loss_function)
epslon = loss_function_grad[np.abs(loss_function_grad - 0).argmin()]

initial_x = random.randint(0, 300)

print(int(epslon))

while(loss_function_grad[int(initial_x)] != epslon):
    if (loss_function_grad[int(initial_x)]>0):
        initial_x -= step
    else:
        initial_x += step
print(x_axe[int(initial_x)])

# plot
fig, ax = mpl.subplots()

ax.plot(x_axe, loss_function)


mpl.show()
