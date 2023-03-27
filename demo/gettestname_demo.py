import inspect

def whoami():
    return inspect.stack() [1][3]

def Myfunctio_TT():
    x = whoami()
    print(x)

Myfunctio_TT()