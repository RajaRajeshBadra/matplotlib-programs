#Plot tan(x), cot(x), sec(x) and cosec(x) for the values of x= [-pi,-pi/4, -pi/2, 0, pi/4, pi/2, pi].
import numpy as np
import matplotlib.pyplot as plt

def q1():
    pi = np.pi
    vals = np.array([-pi, -pi/4, -pi/2, 0, pi/4, pi/2, pi])
    tan, cot, sec, cosec = np.tan(vals), 1/np.tan(vals), 1/np.cos(vals), 1/np.sin(vals)
    plt.plot(vals, tan, label = 'Tan(x)')
    plt.plot(vals, cot, label = 'Cot(x)')
    plt.plot(vals, sec, label = 'Sec(x)')
    plt.plot(vals, cosec, label = 'Cosec(x)')
    plt.legend()
    plt.show()

q1()