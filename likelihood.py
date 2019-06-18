# -*- coding: utf-8 -*-
"""
Created on Tue May  6 11:08:16 2014

@author: kenjakt
"""
import numpy as np
import sympy
from sympy.utilities.lambdify import lambdify
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr

def likelihood(T,dT,Lambda,X,model):
    mu=X[0]
    alpha=X[1]
    
    if model=='Mooney-Rivlin':
                      ## Mooney-Rivlin Model
        sigma = lambda x: 2*mu*x+2*alpha-2*mu*x**(-2)-2*alpha*x**(-3)
        return -sum((sigma(Lambda)-T)**2/(2*dT**2))

    elif model=='Exponential':
        if alpha==sympy.symbols('alpha'):
            sigma=[]
            for x in Lambda:
                sigma.append(2*(x-x**-2)*mu*alpha*sympy.exp(alpha*(x**2+2*x**-1-3)))
            sigma=np.array(sigma)    
            return -sum((sigma-T)**2/(2*dT**2))
        else:
            sigma = lambda x: 2*(x-x**-2)*mu*alpha*np.exp(alpha*(x**2+2*x**-1-3))
            return -sum((sigma(Lambda)-T)**2/(2*dT**2))

    elif model=='Ogden': 
                  ## 1-Term Ogden Model
        sigma = lambda x: 2*mu/alpha*(x**(alpha-1)-x**(-1-alpha/2))
        return -sum((sigma(Lambda)-T)**2/(2*dT**2))
    else:
        model_expr=parse_expr(model[0].rstrip())
        param1,param2,x=symbols('param1 param2 x')
        temp=lambdify((x,param1,param2),model_expr,"numpy")
        if alpha==sympy.symbols('alpha'):
            cov_list=[]
            der_model_expr_param1 = parse_expr(model[1].rstrip())
            der_model_expr_param2 = parse_expr(model[2].rstrip())
            sec_der_model_expr_param1 = parse_expr(model[3].rstrip())
            sec_der_model_expr_param2 = parse_expr(model[4].rstrip())
            sec_der_model_expr_param1_param2 = parse_expr(model[5])
            
            der_mu_2_temp1 = (der_model_expr_param1**2 + sec_der_model_expr_param1*(model_expr - T))/dT**2
            der_mu_2_temp2 = np.array([lambdify((x,param1,param2),i,"numpy") for i in der_mu_2_temp1])
            i=0
            der_mu_2=[]
            for j in der_mu_2_temp2:
                der_mu_2.append(j(Lambda[i],param1,param2))
                i+=1
            der_mu_2=np.array(der_mu_2)
            der_mu_2=-sum(der_mu_2)
            der_mu_2=lambdify((param1,param2),der_mu_2,"numpy")
            cov_list.append(der_mu_2)
            
            der_alpha_2_temp1 = (der_model_expr_param2**2 + sec_der_model_expr_param2*(model_expr - T))/dT**2
            der_alpha_2_temp2 = np.array([lambdify((x,param1,param2),i,"numpy") for i in der_alpha_2_temp1])
            i=0
            der_alpha_2=[]
            for j in der_alpha_2_temp2:
                der_alpha_2.append(j(Lambda[i],param1,param2))
                i+=1
            der_alpha_2=np.array(der_alpha_2)
            der_alpha_2=-sum(der_alpha_2)
            der_alpha_2=lambdify((param1,param2),der_alpha_2)
            cov_list.append(der_alpha_2)
            
            der_mu_alpha_2_temp1 = (der_model_expr_param1*der_model_expr_param2 + sec_der_model_expr_param1_param2*(model_expr - T))/dT**2
            der_mu_alpha_2_temp2 = np.array([lambdify((x,param1,param2),i,"numpy") for i in der_mu_alpha_2_temp1])
            i=0
            der_mu_alpha_2=[]
            for j in der_mu_alpha_2_temp2:
                der_mu_alpha_2.append(j(Lambda[i],param1,param2))
                i+=1
            der_mu_alpha_2=np.array(der_mu_alpha_2)
            der_mu_alpha_2=-sum(der_mu_alpha_2)
            der_mu_alpha_2=lambdify((param1,param2),der_mu_alpha_2)
            cov_list.append(der_mu_alpha_2)
            return cov_list
        else:
            sigma=lambdify(x,temp(x,mu,alpha))
            return -sum((sigma(Lambda)-T)**2/(2*dT**2))
            