import random as rnd
import time

import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
from termcolor import colored

# ---------------------------------- FUNCTION SECTION -----------------------------------------
# You can add any function below to a with its options 

# This is the function
w = sy.Symbol('w')
func_list ={'a':{'equation':0.1*(w-18)**2 + 1,
                 'range':[-5, 30],
                 'optimal':[18, 1],
                 'y_limit':[0, 50], 
                 'epslon':0.01,
                 'step':0.01,
                },
            'b':{'equation':10*(w-5)**2/(1+(w-5)**2)+1.3,
                 'range':[-6, 16],
                 'optimal':[5, 1.3],
                 'y_limit':[0, 14],
                 'epslon':0.04,
                 'step':0.001,
                }}
# ----------------------------------------- END -----------------------------------------------


# ---------------------------------- INPUT SECTION --------------------------------------------
print("Please choose one of the equations below :")
print(f"---------- EQUATION '{colored('a', 'red', attrs=['underline'])}'--------")
sy.printing.pprint(func_list['a']['equation'], use_unicode=True)
print('\n')
print(f"---------- EQUATION '{colored('b', 'red', attrs=['underline'])}'--------")
sy.printing.pprint(func_list['b']['equation'], use_unicode=True)
print('\n')

user_inp = input(f"{colored('Yor choise > ', 'green', attrs=['underline'])}")
# ----------------------------------------- END -----------------------------------------------


# ---------------------------------- CONTROLL SECTION -----------------------------------------
# You can edit these parameters below to get different results👇

# The initial point will be selected wethen this range
x_axis_range = [func_list[user_inp]['range'][0], func_list[user_inp]['range'][1]]  
step = func_list[user_inp]['step']      # The amount of increase/decrease to be applied on W
time_between_itr = 0.00                 # controll the speed of the output on the console (time in sec)
epslon = func_list[user_inp]['epslon']  # IMPORTANT: to detrmin when to stop searching (closest to zero) 
digits = 5                              # Output numbers pression (No of digits)
y_limit = func_list[user_inp]['y_limit']                               
counter = 0

# Randome initial point to start the search from
loss_gradient = sy.diff(func_list[user_inp]['equation'])  # The derevative of the function
initial_w = rnd.uniform(x_axis_range[0], x_axis_range[1]) # Randome initial point to start the search from
final_w = initial_w
# ----------------------------------------- END -----------------------------------------------

# The algorethim starts here
while(list(loss_gradient.subs({w:final_w}).atoms())[0] < -epslon or list(loss_gradient.subs({w:final_w}).atoms())[0] > epslon):
    wk_gradient = list(loss_gradient.subs({w:final_w}).atoms())[0]
    if (wk_gradient > 0):
        final_w -= step
    else:
        final_w += step
    time.sleep(time_between_itr)
    print(f"Iam now at > {colored(round(final_w, digits), 'yellow')}")
    counter+=1

print(f"""\nSearch startd from {colored(round(initial_w, digits), 'magenta', attrs=['blink'])}
The least error for this wight is found at 👉 {colored(round(final_w, digits), 'green', attrs=['blink'])} 
With loss value of {colored(round(func_list[user_inp]['equation'].evalf(subs={w:final_w}), digits), 'cyan')}
solution found using {colored(counter, 'blue')} iterations 
\nThe final gradient value is {colored(round(wk_gradient, digits), 'magenta')}""")

# ---------------------------------- VISUALIZATION SECTION -----------------------------------------
x_axe = np.linspace(x_axis_range[0], x_axis_range[1], 2000)

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
fig.set_figwidth(9)
fig.set_figheight(9)

ax.set_facecolor('#e5ecf6')
ax.set_title(f"${sy.printing.latex(func_list[user_inp]['equation'])}$")
ax.set_ylabel('Loss')
ax.set_xlabel('Wight')
plt.ylim(y_limit[0], y_limit[1])
ax.grid(which='major', color='#f7f9fd', linewidth=1.3)

ax.plot(x_axe, list((func_list[user_inp]['equation'].evalf(subs={w:x}) for x in x_axe)),zorder=1, color='#616cfa', label='Loss func')
ax.scatter(initial_w, func_list[user_inp]['equation'].evalf(subs={w:initial_w}), label = 'Init value',color='#F3BC50',zorder=3, s=65, marker = 'x')
ax.scatter(func_list[user_inp]['optimal'][0], func_list[user_inp]['optimal'][1], label = 'Desired value', s=80, color='#00cc96',zorder=2, marker = 'o')
ax.scatter(final_w, func_list[user_inp]['equation'].evalf(subs={w:final_w}), label = 'Actual value',color='#ff6238',zorder=3, s=80, marker = '.')

fig.legend()
plt.show(block=True)
# ------------------------------------------ END -----------------------------------------------