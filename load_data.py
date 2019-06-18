# -*- coding: utf-8 -*-
"""
Created on Tue May  6 11:40:41 2014

@author: kenjakt

Display data
"""

import matplotlib.pyplot as plt
import numpy as np

def load_data(filename):
	data = np.genfromtxt(filename, delimiter=',')
	stretch = data[0]
	experimentalStress = data[1]
	delta = data[2]
	
	fig = plt.figure()
	plt.errorbar(stretch, experimentalStress, delta, capsize=4, ecolor='r', marker='o', ms=2.0, fillstyle='none')

	return data, fig
