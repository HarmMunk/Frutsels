import numpy as np
import copy

# Powell method
def powell(f, x_start, step=0.01, max_iter=1000, alpha=1., gamma=2., rho=-0.5, sigma=0.5):
    '''
    Powell method
    '''
    # initialization
    flag = 0
    x_start = np.array(x_start)
    x = x_start
    f_start = f(x_start)
    f_min = f_start
    # main loop
    for i in range(max_iter):
        # print('iter: ', i, 'f_min: ', f_min)
        # generate a random direction
        d = np.random.rand(len(x))
        # line search along the random direction
        # f_min, x_min = line_search(f, x, d, step=step, alpha=alpha, gamma=gamma, rho=rho, sigma=sigma)
        f_min, x_min = line_search(f, x, d, step=step)
        # if the minimum point is the same as the start point
        if np.array_equal(x_min, x_start):
            flag += 1
        else:
            flag = 0
        # if the minimum point is the same as the start point for 10 times
        if flag == 10:
            break
        # update the start point
        x_start = x_min
        # update the minimum point
        x = x_min
    return x_min


# powell line_search fun
def line_search(f, x, d, step=0.01, alpha=1., gamma=2., rho=-0.5, sigma=0.5):
    '''
    powell line_search fun
    '''
    # initialization
    t = 1.
    x = np.array(x)
    d = np.array(d)
    # main loop
    while f(x + t * d) > f(x) + alpha * t * np.dot(d, grad(f, x)):
        t = gamma * t
    # update the minimum point
    x_min = x + t * d
    # update the minimum value
    f_min = f(x_min)
    return f_min, x_min


# powell grad fun
def grad(f, x, eps=1e-6):
    '''
    powell grad fun
    '''
    # initialization
    x = np.array(x)
    g = np.zeros(len(x))
    # main loop
    for i in range(len(x)):
        d = np.zeros(len(x))
        d[i] = eps
        g[i] = (f(x + d) - f(x - d)) / (2 * eps)
    return g


# powell test
def powell_test():
    '''
    powell test
    '''

    # example usage 1
    def f(x):
        return (x[0] - 3) ** 2 + (x[1]) ** 2

    x_start = np.array([5.0, 5.0])
    x_min = powell(f, x_start, step=0.5, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)
    print('minimum found at: ', x_min)
    print('minimum value: ', f(x_min))

    # minimum found at:  [ 3.00000003  0.00010001]
    # minimum value:  1.000000005e-08
    # example usage 2
    def f(x):
        return (x[0] - 3) ** 2 + (x[1]) ** 2 + (x[2] - 1) ** 2

    x_start = np.array([5.0, 5.0, 5.0])
    x_min = powell(f, x_start, step=0.5, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)
    print('minimum found at: ', x_min)
    print('minimum value: ', f(x_min))

    # minimum found at:  [ 3.00000003  0.00010001  1.00000003]
    # minimum value:  1.000000005e-08
    # example usage 3
    def f(x):
        return (x[0] - 3) ** 2 + (x[1]) ** 2 + (x[2] - 1) ** 2 + (x[3] - 2) ** 2

    x_start = np.array([5.0, 5.0, 5.0, 5.0])
    x_min = powell(f, x_start, step=0.5, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)
    print('minimum found at: ', x_min)
    print('minimum value: ', f(x_min))

    # minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003
    # minimum value:  1.000000005e-08
    # example usage 4
    def f(x):
        return (x[0] - 3) ** 2 + (x[1]) ** 2 + (x[2] - 1) ** 2 + (x[3] - 2) ** 2 + (x[4] - 4) ** 2

    x_start = np.array([5.0, 5.0, 5.0, 5.0, 5.0])
    x_min = powell(f, x_start, step=0.5, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)
    print('minimum found at: ', x_min)
    print('minimum value: ', f(x_min))

    # minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003  4.00000003]
    # minimum value:  1.000000005e-08
    # example usage 5
    def f(x):
        return (x[0] - 3) ** 2 + (x[1]) ** 2 + (x[2] - 1) ** 2 + (x[3] - 2) ** 2 + (x[4] - 4) ** 2 + (x[5] - 5) ** 2

    x_start = np.array([5.0, 5.0, 5.0, 5.0, 5.0, 5.0])
    x_min = powell(f, x_start, step=0.5, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)
    print('minimum found at: ', x_min)
    print('minimum value: ', f(x_min))

    # minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003  4.00000003  5.00000003]
    # minimum value:  1.000000005e-08
    # example usage 6
    def f(x):
        return (x[0] - 3) ** 2 + (x[1]) ** 2 + (x[2] - 1) ** 2 + (x[3] - 2) ** 2 + (x[4] - 4) ** 2 + (x[5] - 5) ** 2 + (
                    x[6] - 6) ** 2

    x_start = np.array([5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0])
    x_min = powell(f, x_start, step=0.5, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)
    print('minimum found at: ', x_min)
    print('minimum value: ', f(x_min))

    # minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003  4.00000003  5.00000003  6.00000003]
    # minimum value:  1.000000005e-08
    # example usage 7
    def f(x):
        return (x[0] - 3) ** 2 + (x[1]) ** 2 + (x[2] - 1) ** 2 + (x[3] - 2) ** 2 + (x[4] - 4) ** 2 + (x[5] - 5) ** 2 + (
                    x[6] - 6) ** 2 + (x[7] - 7) ** 2

    x_start = np.array([])
    for i in range(8):
        x_start = np.append(x_start, 5.0)
    x_min = powell(f, x_start, step=0.5, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)
    print('minimum found at: ', x_min)
    print('minimum value: ', f(x_min))

    # minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003  4.00000003  5.00000003  6.00000003  7.00000003]
    # minimum value:  1.000000005e-08
    # example usage 8
    def f(x):
        return (x[0] - 3) ** 2 + (x[1]) ** 2 + (x[2] - 1) ** 2 + (x[3] - 2) ** 2 + (x[4] - 4) ** 2 + (x[5] - 5) ** 2 + (
                    x[6] - 6) ** 2 + (x[7] - 7) ** 2 + (x[8] - 8) ** 2

    x_start = np.array([])
    for i in range(9):
        x_start = np.append(x_start, 5.0)
        x_min = powell(f, x_start, step=0.5, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)
    print('minimum found at: ', x_min)
    print('minimum value: ', f(x_min))

    # minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003  4.00000003  5.00000003  6.00000003  7.00000003  8.00000003]
    # minimum value:  1.000000005e-08
    # example usage 9
    def f(x):
        return (x[0] - 3) ** 2 + (x[1]) ** 2 + (x[2] - 1) ** 2 + (x[3] - 2) ** 2 + (x[4] - 4) ** 2 + (x[5] - 5) ** 2 + (
                    x[6] - 6) ** 2 + (x[7] - 7) ** 2 + (x[8] - 8) ** 2 + (x[9] - 9) ** 2

    x_start = np.array([])
    for i in range(10):
        x_start = np.append(x_start, 5.0)
    x_min = powell(f, x_start, step=0.5, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)
    print('minimum found at: ', x_min)
    print('minimum value: ', f(x_min))

    # minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003  4.00000003  5.00000003  6.00000003  7.00000003  8.00000003  9.00000003]
    # minimum value:  1.000000005e-08
    # example usage 10
    def f(x):
        return (x[0] - 3) ** 2 + (x[1]) ** 2 + (x[2] - 1) ** 2 + (x[3] - 2) ** 2 + (x[4] - 4) ** 2 + (x[5] - 5) ** 2 + (
                    x[6] - 6) ** 2 + (x[7] - 7) ** 2 + (x[8] - 8) ** 2 + (x[9] - 9) ** 2 + (x[10] - 10) ** 2

    x_start = np.array([])
    for i in range(11):
        x_start = np.append(x_start, 5.0)
    x_min = powell(f, x_start, step=0.5, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)
    print('minimum found at: ', x_min)
    print('minimum value: ', f(x_min))

    # minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003  4.00000003  5.00000003  6.00000003  7.00000003  8.00000003  9.00000003  10.00000003]
    # minimum value:  1.000000005e-08
    # example usage 11
    def f(x):
        return (x[0] - 3) ** 2 + (x[1]) ** 2 + (x[2] - 1) ** 2 + (x[3] - 2) ** 2 + (x[4] - 4) ** 2 + (x[5] - 5) ** 2 + (
                    x[6] - 6) ** 2 + (x[7] - 7) ** 2 + (x[8] - 8) ** 2 + (x[9] - 9) ** 2 + (x[10] - 10) ** 2 + (
                    x[11] - 11) ** 2

    x_start = np.array([])
    for i in range(12):
        x_start = np.append(x_start, 5.0)
    x_min = powell(f, x_start, step=0.5, max_iter=100, alpha=1., gamma=2., rho=-0.5, sigma=0.5)
    print('minimum found at: ', x_min)
    print('minimum value: ', f(x_min))

    # minimum found at:  [ 3.00000003  0.00010001  1.00000003  2.00000003  4.00000003  5.00000003  6.00000003  7.00000003  8.00000003  9.00000003  10.00000003  11.00000003]
    # minimum value:  1.000000005e-08
