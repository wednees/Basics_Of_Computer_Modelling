import numpy as n
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

step = 100
t = n.linspace(0, 2 * n.pi, step)
x = n.sin(t)
phi = n.sin(-t)

fgr = plt.figure()
gr = fgr.add_subplot(1, 1, 1)
gr.axis('equal')

gr.plot([0, 0, 4], [2, 0, 0], linewidth=3)

R = 0.45
r = 0.1
x0 = 1.5
L = 0.35

Xa = x0 + x
Ya = R

Xb = Xa + L * n.sin(phi)
Yb = Ya - L * n.cos(phi)

pA = gr.plot(Xa[0], Ya, marker='o')[0]

Alp = n.linspace(0, 2*n.pi, 100)
Xc = n.cos(Alp)
Yc = n.sin(Alp)

Main_cylinder = gr.plot(Xc * R + Xa[0], Yc * R + Ya)[0]
Sub_cylinder = gr.plot(Xc * r + Xb[0], Yc * r + Yb[0])[0]

Np = 20
Xp = n.linspace(0, 1, 2*Np+1)
Yp = 0.06 * n.sin(n.pi / 2 * n.arange(2*Np+1))

Spring = gr.plot((x0 + x[0]) * Xp, Yp + R)[0]


def run(i):
    pA.set_data([Xa[i]], [Ya])
    Main_cylinder.set_data([Xc * R + Xa[i]], [Yc * R + Ya])
    Sub_cylinder.set_data([Xc * r + Xb[i]], [Yc * r + Yb[i]])
    Spring.set_data((x0 + x[i]) * Xp, Yp + R)
    return [pA, Main_cylinder, Sub_cylinder, Spring]


anim = FuncAnimation(fgr, run, frames=step, interval=1)

plt.show()
