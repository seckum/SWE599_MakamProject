import math
import sys
import os
import numpy as np

class hertztocent:
    def herzToCent(array):
        ref_freq = float(8.17579892*2) 
        centdata=[]
        for i in range(len(array)):
         centdata.append(round(1200*math.log2(array[i]/ref_freq)))
        return centdata

    def normalizeSum(ar):
	    summ = float(0)
	    for i in range(len(ar)):
	     summ = summ+ar[i]
	    for i in range(len(ar)):
	     ar[i] = ar[i]/summ 
		

'''
	def normalizeMax(ar):
		maximum = float(0)
		temp=np.zeros(len(ar),dtype=float)
		temp =ar.copy()
		temp.sort()
		maximum =temp[len(temp)-1]
		norm=[]
		for i in range(len(ar)):
			norm.append(ar[i]/maximum)
		return norm	
'''


	