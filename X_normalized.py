import numpy as np
A=np.arange(1,101).reshape(10,10)
Asquared=A**2
div3=Asquared[Asquared%3==0]
print("")