import numpy as np
import matplotlib.pylab as plt


def add_process_step(cycle, T, duration, ramp=2):
    """
    Add process step starting with ramp and dwell step if duration >0
    duration in min
    Ramp is in K/min
    """
    t_old = cycle[-1, 0]
    T_old = cycle[-1, 1]
    ramp_duration = np.abs((T_old - T) / ramp)
    cycle = np.vstack([cycle, [t_old + ramp_duration, T]])
    if duration > 0:
        cycle = np.vstack([cycle, [cycle[-1, 0] + duration, T]])
    return cycle


def plot_tangent(x0, y0, m, dx, label):
    """Plot tangent"""
    dxi = dx / 5
    x1 = x0 - dxi
    x2 = x0 + dxi
    y1 = y0 - m * dxi
    y2 = y0 + m * dxi
    p, = plt.plot([x1, x2], [y1, y2], label=label)
    color = p.get_color()
    plt.plot(x0, y0, marker="x", mfc=color, mec=color)