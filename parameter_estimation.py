# -*- coding: utf-8 -*-
"""
Created on Thu May 29 13:17:00 2014

@author: kenjakt
"""

import numpy as np
from scipy.optimize import minimize
from Model import Model
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from likelihood import likelihood
import sympy
from sympy import symbols
from sympy.utilities.lambdify import lambdify
from cov_plot import cov_plot

def parameter_estimation(model,f,param_dict):
    if type(model)==list:
        model_expr=model[0].rstrip() 
    else:
        model_expr=model
    
    chosen_model=Model(mtype=model_expr)
    
    if model_expr in param_dict:
        param=param_dict[model_expr]   
        print 'Sol ('+model_expr+') =',param
    else:
        L=lambda P:-likelihood(f[1],f[2],f[0],P,model)
#    parameters={}
    
        Sol=minimize(L,np.array([0.29,4.5]),method='BFGS')     ###minimization
    #             options={'maxfev':1e+08,'maxiter':1e+08} ###and parameter estimation       
        param=Sol.x
        param_dict[model_expr]=Sol.x
        print 'Sol ('+model_expr+') =',param
    
        """Estimate the Posterior PDF - QUADRATIC APPROXIMATION of Likelihood function"""
    if 'C_m'+model_expr in param_dict:
        C_m=param_dict['C_m'+model_expr]
        Alpha=param_dict['Alpha'+model_expr]
        Mu=param_dict['Mu'+model_expr]
        PDF=param_dict['PDF'+model_expr]
    else:
        mu,alpha=symbols('mu alpha')
        Params=[mu,alpha]
        if model=='Ogden' or model=='Exponential' or model=='Mooney-Rivlin':
            L=likelihood(f[1],f[2],f[0],Params,model)
        
            diff_mu_2 = lambdify((mu,alpha),sympy.diff(L,mu,2))
            diff_alpha_2 = lambdify((mu,alpha),sympy.diff(L,alpha,2))
            diff_mu_alpha = lambdify((mu,alpha),
                                     sympy.diff(sympy.diff(L,alpha),mu))
        else:
            cov_list = likelihood(f[1],f[2],f[0],Params,model)
            diff_mu_2 = cov_list[0]
            diff_alpha_2 = cov_list[1]
            diff_mu_alpha = cov_list[2]
        
        A = diff_mu_2(param[0],param[1])
        B = diff_alpha_2(param[0],param[1])
        C = diff_mu_alpha(param[0],param[1])
        
        Sigma_Mu = np.sqrt(-B/(A*B-C**2))
        Sigma_alpha = np.sqrt(-A/(A*B-C**2))
        Sigma_Mu_alpha = np.sqrt(C/(A*B-C**2)+0j)
        
        print 'Sigma_Mu =',Sigma_Mu,'\n','Sigma_alpha =',Sigma_alpha,'\n','Sigma_Mu_alpha =',Sigma_Mu_alpha
        
        """Covariance Matrix"""
        delL=np.array([[A,C],[C,B]])
        C_m=-np.linalg.inv(delL)
        param_dict['C_m'+model_expr]=C_m
         
        #%%============================================================================
        """SAMPLING based estimate of Posterior PDF"""
        
        # Sampling values from [-2*sigma 2*sigma]
        
        Mu = np.r_[param[0]-2*Sigma_Mu:param[0]+2*Sigma_Mu:0.01]
        Alpha = np.r_[param[1]-2*Sigma_alpha:param[1]+2*Sigma_alpha:0.01]
        
        PDF=[]
        for i in range(len(Mu)):
            PDFrow=[]    
            for j in range(len(Alpha)):        
                P = [Mu[i],Alpha[j]]
                PDFrow.append(np.exp(likelihood(f[1],f[2],f[0],P,model)))
            PDF.append(PDFrow)
        PDF=np.array(PDF)
        param_dict['Mu'+model_expr]=Mu
        param_dict['Alpha'+model_expr]=Alpha
        param_dict['PDF'+model_expr]=PDF
        
        """Likelihood at optimal values of Mu and Alpha"""
        Pop = np.exp(likelihood(f[1],f[2],f[0],[param[0],param[1]],model))
        print 'Pop =',Pop
        
        #%%============================================================================
        """Evidence - Volume under the likelihood surface integrated over mu and alpha"""
        mu_max = 0
        mu_min = 10 
        alpha_max = 0
        alpha_min = 20 
        Mu = np.r_[param[0]-2*Sigma_Mu:param[0]+2*Sigma_Mu:0.01]
        Alpha = np.r_[param[1]-2*Sigma_alpha:param[1]+2*Sigma_alpha:0.01]
        Vol_PDF = np.trapz(np.trapz(PDF,Alpha,axis=1),Mu,axis=0)
        Evidence = ((1.0/(mu_max-mu_min))*(1.0/(alpha_max-alpha_min))*Vol_PDF)
        print 'Vol_PDF =',Vol_PDF
        print 'Evidence =',Evidence
        
    #Print Figures
    fig=plt.figure()
    
    plt.subplot(221)
    plt.errorbar(f[0],f[1],f[2],ecolor='r',elinewidth=1,capsize=3) 
    plt.hold(True)
    plt.plot(f[0],chosen_model.T(f[0],param[0],param[1]),linewidth=1)
    plt.grid(True)
    plt.axis('tight')
    plt.hold(False)
    
    plt.subplot(222)
    cov_plot(param[:,np.newaxis],C_m,2,r'$\mu$',r'$\alpha$')

    Alpha,Mu=np.meshgrid(Alpha,Mu)         
    ax_five=fig.add_subplot(223,projection='3d')
    surf_PDF=ax_five.plot_surface(Alpha,Mu,PDF,cmap=cm.coolwarm)
    fig.colorbar(surf_PDF)
    plt.axis('tight')
    #%%============================================================================
    """Comparison - Quadratic Approximation and Samplin"""

    Mu, Alpha, PDF=param_dict['Mu'+model_expr],param_dict['Alpha'+model_expr],param_dict['PDF'+model_expr]
    plt.subplot(224)
    plt.contour(Mu,Alpha,PDF.T)
    plt.hold(True)
    plt.colorbar()
    cov_plot(param[:,np.newaxis],C_m,2,r'$\mu$',r'$\alpha$')
    plt.hold(False)
#    plt.show(plt.figure())
    
    return fig,param_dict
    
