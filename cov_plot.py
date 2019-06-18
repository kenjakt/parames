# -*- coding: utf-8 -*-
"""
Created on Tue May  6 11:06:43 2014

@author: kenjakt
"""
import numpy as np
import matplotlib.pyplot as plt

def cov_plot(M,C,nsd,X,Y):
    npts=50
    theta=np.linspace(0,2*np.pi,npts)
    x=np.cos(theta)
    y=np.sin(theta)
    ap=np.vstack((x,y))
    d,v=np.linalg.eig(C)
    d=nsd*np.sqrt(d)
    bp=(np.dot(np.dot(v,np.diag(d)),ap)) + np.tile(M,(1,np.shape(ap)[1]))
    h=plt.plot(bp[0],bp[1],'b-',linewidth=3.0)
    plt.xlabel(X,fontsize=14)
    plt.ylabel(Y,fontsize=14)
    plt.axis('tight')
    return h