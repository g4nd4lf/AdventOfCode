import time
import numpy as np
def on(c):
    d=c.copy()
    d.remove(2)
    return d
a=set()
a.add(1)
a.add(2)
a.add(3)
b=on(a)
print(a)
print(b)


                
    