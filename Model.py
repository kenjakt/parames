# -*- coding: utf-8 -*-
"""
Parameter Estimation/Model self.Calibration/Model Selection
"""
import numpy as np
from sympy.utilities.lambdify import lambdify
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr

class Model():
    def __init__(self,mtype):
        self.mtype=mtype
        if self.mtype=='Ogden':
            self.T=lambda x,y0,y1:((2*y0/y1)*(x**(y1-1)-x**(-1-y1/2)))
        elif self.mtype=='Mooney-Rivlin':
            self.T=lambda x,y0,y1: 2*y0*x+2*y1-2*y0*x**(-2)-2*y1*x**(-3)
        elif self.mtype=='Exponential':
            self.T=lambda x,y0,y1: 2*(x-x**(-2))*y0*y1*np.exp(y1*(x**2+2*x**(-1)-3))
        else:
            x,param1,param2=symbols('x param1 param2')
#            params=[param1,param2]
            self.T=lambdify((x,param1,param2),parse_expr(mtype),"numpy")
        
#        self.L=lambda P:-likelihood(self.data[1],self.data[2],self.data[0],P,mtype)
#        
#        self.Sol=minimize(self.L,np.array([0.29,4.5]),method='nelder-mead',
#                          options={'maxfev':1e+08,'maxiter':1e+08})
#                          
#        plt.figure()
#        plt.errorbar(self.data[0],self.data[1],self.data[2],
#                     ecolor='r',elinewidth=1,fmt=None)
#        plt.plot(self.data[0],self.T(self.data[0],self.Sol.x),linewidth=1)
#        plt.grid(True)
#        plt.axis('tight')
#        """
#        Estimate the Posterior PDF - 
#        QUADRATIC APPROXIMATION of Likelihood function
#        """
#        mu,alpha=symbols('mu alpha')
#        Params=[mu,alpha]
#        self.new_L=likelihood(self.data[1],self.data[2],self.data[0],Params,mtype)
#
#        self.diff_mu_2 = lambdify((mu,alpha),sympy.diff(self.new_L,mu,2))
#        self.diff_alpha_2 = lambdify((mu,alpha),sympy.diff(self.new_L,alpha,2))
#        self.diff_mu_alpha = lambdify((mu,alpha),
#                         sympy.diff(sympy.diff(self.new_L,alpha),mu))
#                         
#        self.A = self.diff_mu_2(self.Sol.x[0],self.Sol.x[1])
#        self.B = self.diff_alpha_2(self.Sol.x[0],self.Sol.x[1])
#        self.C = self.diff_mu_alpha(self.Sol.x[0],self.Sol.x[1])
#
#        self.Sigma_Mu = np.sqrt(-self.B/(self.A*self.B-self.C**2))
#        self.Sigma_alpha = np.sqrt(-self.A/(self.A*self.B-self.C**2))
#        self.Sigma_Mu_alpha = np.sqrt(self.C/(self.A*self.B-self.C**2)+0j)
#
##Covariance Matrix
#        self.delL=np.array([[self.A,self.C],[self.C,self.B]])
#        self.C_m=-np.linalg.inv(self.delL)
#
##Covariance Matrix Ellipse
#        plt.figure(4)
#        cov_plot(self.Sol.x[:,np.newaxis],self.C_m,2,r'$\mu$',r'$\alpha$')