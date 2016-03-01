# import Kernel_Estimation_v6 as MonImage
import Mes_Fonctions_v2 as MesFonctions
from random import random
import matplotlib.pyplot as pl
import math
import numpy as np
import copy
import opkpy_v3_1


def rosenbrock(x):
    return (x[0] - 1) * (x[0] - 1) + 10 * (x[0] * x[0] - x[1] * x[1]) * (x[0] * x[0] - x[1] * x[1])



def fg_rosen(x, gx):
    gx[0] = 2 * (x[0] - 1) + 40 * x[0] * (x[0] * x[0] - x[1] * x[1])
    gx[1] = -40 * x[1] * (x[0] * x[0] - x[1] * x[1])
    return rosenbrock(x)


if __name__ == "__main__":
    opt = opkpy_v3_1.Optimizer()
    x = np.array([-1.2, 1.0], dtype="float32")
    g = np.array([1, 2], dtype="float32")
    f = fg_rosen(x, g)

    print("INPUT:" + str(x))
    opt.minimize(x, fg_rosen, g, maxiter=5, maxeval=20, verbose=True, bl=1.0)
    print("OUTPUT:" + str(x))