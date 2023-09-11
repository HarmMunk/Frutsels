def f():
    my_val = 1
    print(locals())
    locals()['my_val'] = 2
    print(locals())


for i, j in [[0,1],[1,2]]:
    print(f"i: {i}, j: {j}")
