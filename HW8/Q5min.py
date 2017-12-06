import numpy as np
from scipy.optimize import minimize

def f(x):
    return max(x**2+1,2*x**2+2-2*x*np.sqrt(x**2+1))
    
res = minimize(f,0.1, method='nelder-mead', options={'xtol': 1e-10, 'disp': True})    