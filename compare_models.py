# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:57:18 2014

@author: kenjakt
"""

import matplotlib.pyplot as plt
from scipy.optimize import minimize
from Model import Model
from likelihood import likelihood
import numpy as np
    
def compare_models(to_compare,f,param_dict):
#    models=to_compare.split()
    fig=plt.figure()
    for i in to_compare:
        if i in param_dict:
            param=param_dict[i]
        else:
            L=lambda P:-likelihood(f[1],f[2],f[0],P,i)

            Sol=minimize(L,np.array([0.29,4.5]),method='BFGS')
#                         options={'maxfev':1e+08,'maxiter':1e+08}
            param_dict[i]=Sol.x
            param=Sol.x
    
        to_print_model=Model(i)
        plt.plot(f[0],to_print_model.T(f[0],param[0],param[1]),linewidth=1,label=i)
        plt.hold(True)
    
    plt.errorbar(f[0],f[1],f[2],
                 ecolor='r',elinewidth=1,capsize=3) 
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc=0)
    plt.hold(False)
    return fig,param_dict
    
