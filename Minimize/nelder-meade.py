#  Nelder and Mead minimize function
# for a function of n variables

import numpy as np
import copy


def minimize(f, x_start, step=1.0, no_improve_thr=10e-6,
             no_improv_break=10, max_iter=0, alpha=1., gamma=2.,
             rho=-0.5, sigma=0.5):
    """
        f (function): function to minimize
        x_start (numpy array): initial position
        step (float): look-around radius in initial step
        no_improv_thr,  no_improv_break (float, int): break after no_improv_break iterations with
            an improvement lower than no_improv_thr
        max_iter (int): always break after this number of iterations.
            Set it to 0 to loop indefinitely.
        alpha, gamma, rho, sigma (floats): parameters of the algorithm
            (see Wikipedia page for reference)
        return: tuple (best parameter array, best function value)
    """

    # init
    dim = len(x_start)
    prev_best = f(x_start)
    no_improv = 0
    res = [[x_start, prev_best]]
    for i in range(dim):
        x = copy.copy(x_start)
        x[i] = x[i] + step
        score = f(x)
        res.append([x, score])

    # simplex iter
    iters = 0
    while True:
        # order
        res.sort(key=lambda x: x[1])
        best = res[0][1]

        # break after max_iter
        if max_iter and iters >= max_iter:
            return res[0]
        iters += 1

        # break after no_improv_break iterations with no improvement
        print('...best so far:', best)

        if best < prev_best - no_improve_thr:
            no_improv = 0
            prev_best = best
        else:
            no_improv += 1

        if no_improv >= no_improv_break:
            return res[0]

        # centroid
        x0 = [0.] * dim
        for tup in res[:-1]:
            for i, c in enumerate(tup[0]):
                x0[i] += c / (len(res)-1)

        # reflection
        xr = x0 + alpha*(x0 - res[-1][0])
        rscore = f(xr)
        if res[0][1] <= rscore < res[-2][1]:
            del res[-1]
            res.append([xr, rscore])
            continue

        # expansion
        if rscore < res[0][1]:
            xe = x0 + gamma*(x0 - res[-1][0])
            escore = f(xe)
            if escore < rscore:
                del res[-1]
                res.append([xe, escore])
                continue
            else:
                del res[-1]
                res.append([xr, rscore])
                continue

        # contraction
        xc = x0 + rho*(x0 - res[-1][0])
        cscore = f(xc)
        if cscore < res[-1][1]:
            del res[-1]
            res.append([xc, cscore])
            continue

        # reduction
        x1 = res[0][0]
        nres = []
        for tup in res:
            redx = x1 + sigma*(tup[0] - x1)
            score = f(redx)
            nres.append([redx, score])
            res = nres
        return res[0]

# example usage 1
def f(x):
    return x[0]**2 + x[1]**2

x_start = np.array([1.0, 1.0])
x_min = minimize(f, x_start, step=0.5, no_improve_thr=1e-6, no_improv_break=10, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)[0]
print('minimum found at: ', x_min)
print('minimum value: ', f(x_min))
# minimum found at:  [  1.00912293e-06   1.00912293e-06]
# minimum value:  2.01825169029e-12
breakpoint()
# example usage 2
def f(x):
    return (x[0]-3)**2 + (x[1])**2

x_start = np.array([5.0, 5.0])
x_min = minimize(f, x_start, step=0.5, no_improve_thr=1e-6, no_improv_break=10, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)[0]
print('minimum found at: ', x_min)
print('minimum value: ', f(x_min))
# minimum found at:  [ 3.00000003  0.00010001]
# minimum value:  1.000000005e-08
breakpoint()

# example usage 3
def f(x):
    return (x[0]-3)**2 + (x[1])**2 + (x[2]-1)**2
x_start = np.array([5.0, 5.0, 5.0])
x_min = minimize(f, x_start, step=0.5, no_improve_thr=1e-6, no_improv_break=10, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)[0]
print('minimum found at: ', x_min)
print('minimum value: ', f(x_min))
# minimum found at:  [ 3.00000003  0.00010001  1.00000003]
# minimum value:  1.000000005e-08
breakpoint()

# example usage 4
def f(x):
    return (x[0]-3)**2 + (x[1])**2 + (x[2]-1)**2 + (x[3]-2)**2

x_start = np.array([5.0, 5.0, 5.0, 5.0])
x_min = minimize(f, x_start, step=0.5, no_improve_thr=1e-6, no_improv_break=10, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)[0]
print('minimum found at: ', x_min)
print('minimum value: ', f(x_min))
# minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003]
# minimum value:  1.000000005e-08
breakpoint()

# example usage 5
def f(x):
    return (x[0]-3)**2 + (x[1])**2 + (x[2]-1)**2 + (x[3]-2)**2 + (x[4]-4)**2

x_start = np.array([5.0, 5.0, 5.0, 5.0, 5.0])
x_min = minimize(f, x_start, step=0.5, no_improve_thr=1e-6, no_improv_break=10, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)[0]
print('minimum found at: ', x_min)
print('minimum value: ', f(x_min))
# minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003  4.00000003]
# minimum value:  1.000000005e-08
breakpoint()

# example usage 6
def f(x):
    return (x[0]-3)**2 + (x[1])**2 + (x[2]-1)**2 + (x[3]-2)**2 + (x[4]-4)**2 + (x[5]-5)**2

x_start = np.array([5.0, 5.0, 5.0, 5.0, 5.0, 5.0])
x_min = minimize(f, x_start, step=0.5, no_improve_thr=1e-6, no_improv_break=10, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)[0]
print('minimum found at: ', x_min)
print('minimum value: ', f(x_min))
# minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003  4.00000003  5.00000003]
# minimum value:  1.000000005e-08
breakpoint()

# example usage 7
def f(x):
    return (x[0]-3)**2 + (x[1])**2 + (x[2]-1)**2 + (x[3]-2)**2 + (x[4]-4)**2 + (x[5]-5)**2 + (x[6]-6)**2

x_start = np.array([5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0])
x_min = minimize(f, x_start, step=0.5, no_improve_thr=1e-6, no_improv_break=10, max_iter=1000, alpha=1., gamma=2., rho=-0.5, sigma=0.5)[0]
print('minimum found at: ', x_min)
print('minimum value: ', f(x_min))
# This start value will get minimize trapped in a local minimum at:
# [3.57092761 1.25956104 1.183771   3.16447694 5.0983288  6.27455997 7.51768794]
# with minimum value: 8.436436624953457
x_start = np.array([4.0, 1.0, 2.0, 1.5, 5.0, 5.0, 6.5])
x_min = minimize(f, x_start, step=0.5, no_improve_thr=1e-6, no_improv_break=10, max_iter=10000, alpha=1., gamma=2., rho=-0.5, sigma=0.5)[0]
print('minimum found at: ', x_min)
print('minimum value: ', f(x_min))
# minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003  4.00000003  5.00000003  6.00000003]
# minimum value:  1.000000005e-08