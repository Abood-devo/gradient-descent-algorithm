import math
import random as rnd
import time

import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
from matplotlib import animation
from termcolor import colored

# ---------------------------------- FUNCTION SECTION -----------------------------------------
# You can change the function below to a different one 

# This is the function
w = sy.Symbol('w')
func_list ={'A':{'equation':0.1*(w-18)**2 + 1, 'range':[-10, 30], 'time_itr':0.01, 'epslon':0.03},
            'B':{'equation':(3-w)**10 + (w-3.7)**2 + 1, 'range':[-5, 10], 'time_itr':0.01, 'epslon':0.03},
            'C':{'equation':w**(0.3*math.exp(1)) + w**-math.exp(1), 'range':[0, 30], 'time_itr':0.01, 'epslon':0.03},
            'D':{'equation':-((w+1)**(0.6 * math.exp(1)) + (w+3)**(0.13 * math.exp(1)) - w**2) + 3, 'range':[-2, 10], 'time_itr':0.01, 'epslon':0.03}}
# func_list = 0.1*(w-18)**2 + 1                 # optimal (18, 1)  Best Range                      
# func_list = (3-w)**10 + (w-3.7)**2 + 1      # optimal (3.626, 1.0147)
# ----------------------------------------- END -----------------------------------------------


# ---------------------------------- INPUT SECTION --------------------------------------------
user_inp = input("""Please choose one of the equations below :
A- 0.1*(w-18)^2+1                        "quadratic"
B- (3-w)^10+(w-3.7)^2+1                  "quadratic"
C- w^(0.3*e)+w^-e                        "exponential"
D- -((w+1)^(0.6*e)+(w+3)^(0.13*e)-w^2)+3 "exponential""")
# ----------------------------------------- END -----------------------------------------------


# ---------------------------------- CONTROLL SECTION -----------------------------------------
# You can edit these parameters below to get different results👇

# The initial point will be selected wethen this range
x_axis_range = [func_list[user_inp]['range'][0], func_list[user_inp]['range'][1]]  
step = 0.01                  # The amount of increase/decrease to be applied on W
time_between_itr = 0.001     # controll the speed of the output on the console (time in sec)
epslon = 0.03                # IMPORTANT: to detrmin when to stop searching (closest to zero) 
digits = 5                   # Output numbers pression (No of digits)
counter = 0

# Randome initial point to start the search from
loss_gradient = sy.diff(func_list[user_inp]['equation'])  # The derevative of the function
initial_w = rnd.uniform(x_axis_range[0], x_axis_range[1]) # Randome initial point to start the search from
final_w = initial_w
# ----------------------------------------- END -----------------------------------------------


# printing initial point 
print(f"\nThe Search will start from {colored(round(initial_w, digits), 'magenta', attrs=['blink'])}\n")

no_need = input(f"\nPRESS {colored('Enter', attrs=['bold'])} to start... \nOR {colored('type exit', attrs=['bold'])} to stop  ")

if (no_need == 'exit'):
    exit()
# The algorethim starts here
while(list(loss_gradient.subs({w:final_w}).atoms())[0] < 0 or list(loss_gradient.subs({w:final_w}).atoms())[0] > epslon):
    wk_gradient = list(loss_gradient.subs({w:final_w}).atoms())[0]
    if (wk_gradient > 0):
        final_w -= step
    else:
        final_w += step
    time.sleep(time_between_itr)
    print(f"Iam now at > {colored(round(final_w, digits), 'yellow')}")
    counter+=1

print(f"""\nThe least error for this wight is found at 👉 {colored(round(final_w, digits), 'green', attrs=['blink'])} 
with func_list value of {colored(round(func_list[user_inp]['equation'].evalf(subs={w:final_w}), digits), 'cyan')}
with {colored(counter, 'blue')} iterations 
\nThe final gradient value is {colored(round(wk_gradient, digits), 'magenta')}""")

# ---------------------------------- VISUALIZATION SECTION -----------------------------------------
x_axe = np.linspace(x_axis_range[0], x_axis_range[1], 1000)

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
fig.set_figwidth(9)
fig.set_figheight(9)

ax.set_facecolor('#e5ecf6')
ax.set_title(f"${sy.printing.latex(func_list[user_inp]['equation'])}$")
ax.set_ylabel('Loss')
ax.set_xlabel('Wight')
plt.ylim(-10, 50)
ax.grid(which='major', color='#f7f9fd', linewidth=1.3)

ax.plot(x_axe, list((func_list[user_inp]['equation'].evalf(subs={w:x}) for x in x_axe)),zorder=1, color='#616cfa', label='Loss func')
ax.scatter(initial_w, func_list[user_inp]['equation'].evalf(subs={w:initial_w}), label = 'Init value',color='#F3BC50',zorder=3, s=65, marker = 'x')
ax.scatter(18, 1, label = 'Desired value', s=80, color='#00cc96',zorder=2, marker = 'o')
ax.scatter(final_w, func_list[user_inp]['equation'].evalf(subs={w:final_w}), label = 'Actual value',color='#ff6238',zorder=3, s=80, marker = '.')

fig.legend()
plt.show()

# ------------------------------------------ END -----------------------------------------------





