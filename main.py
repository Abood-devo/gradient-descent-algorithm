import random as rnd
import time

import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
from termcolor import colored

# ---------------------------------- CONTROLL SECTION -----------------------------------------
# You can edit these parameters below to get different results👇

step = 0.01                  # The amount of increase/decrease to be applied on W
x_axis_range = [0, 30]       # The initial point will be selected wethen this range
time_between_itr = 0.001     # controll the speed of the output on the console (time in sec)
epslon = 0.03                # IMPORTANT: to detrmin when to stop searching (closest to zero) 
# ----------------------------------------- END -----------------------------------------------

# ---------------------------------- FUNCTION SECTION -----------------------------------------
# You can change the function below to a different one 

w = sy.Symbol('w')
loss = 0.1*(w-18)**2 + 1                                  # This is the function
loss_gradient = sy.diff(loss)                             # The derevative of the function
initial_w = rnd.uniform(x_axis_range[0], x_axis_range[1]) # Randome initial point to start the search from
# ----------------------------------------- END -----------------------------------------------

counter = 0

# printing initial point 
print(f"\nThe Search will start from {colored(round(initial_w, 5), 'magenta', attrs=['blink'])}\n")
time.sleep(1)

# The algorethim starts here
while(list(loss_gradient.subs({w:initial_w}).atoms())[0] < 0 or list(loss_gradient.subs({w:initial_w}).atoms())[0] > epslon):
    wk_gradient = list(loss_gradient.subs({w:initial_w}).atoms())[0]
    if (wk_gradient > 0):
        initial_w -= step
    else:
        initial_w += step
    time.sleep(time_between_itr)
    print(f"Iam now at > {colored(round(initial_w, 5), 'yellow')}")
    counter+=1

print(f"""\nThe least error for this wight is found at 👉 {colored(round(initial_w, 5), 'green', attrs=['blink'])} 
with loss value of {colored(loss.evalf(subs={w:initial_w}), 'cyan')}
with {colored(counter, 'blue')} iterations 
\nThe final loss value is {colored(round(wk_gradient, 5), 'magenta')}""")

# ---------------------------------- VISUALIZATION SECTION -----------------------------------------
x_axe = np.linspace(x_axis_range[0], x_axis_range[1], 1000)

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.set_facecolor('#e5ecf6')
ax.set_title(f'${sy.printing.latex(loss)}$')
ax.set_ylabel('Loss')
ax.set_xlabel('Wight')
fig.set_figwidth(9)
fig.set_figheight(9)
ax.plot(x_axe, list((loss.evalf(subs={w:x}) for x in x_axe)),zorder=1, color='#616cfa', label='Loss func')
ax.scatter(initial_w, loss.evalf(subs={w:initial_w}), label = 'Actual value',color='#ff6238',zorder=3, s=80, marker = 'o')
ax.scatter(18, 1, label = 'Desired value', s=80, color='#00cc96',zorder=2, marker = 'o')
ax.grid(which='major', color='#f7f9fd', linewidth=1.3)
fig.legend()
plt.show()

# ----------------------------------------- END -----------------------------------------------





