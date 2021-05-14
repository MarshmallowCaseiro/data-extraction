#########################  import packages  ##########################################
import numpy as np
import csv
import math
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib import interactive
import os
import random
#################### Tri des donnees   ################################################

with open("plot_over_line_data.csv","r") as file_source:
	file_plot = csv.reader(file_source)
#	file_plot.next()
	with open("result.txt","w") as result:
		wtr= csv.writer(result)
		for row in file_plot :
			wtr.writerow( (row[0],row[1], row[2],  row[20], row[21], row[22])) # U0, U1, U2, X, Y, Z

data = np.genfromtxt("result.txt",delimiter=',');

### data storage ####
U0	 	  = data[:,0]
U1	  	  = data[:,1]
U2      	  = data[:,2]
X     		  = data[:,3]
Y		  = data[:,4]
Z		  = data[:,5]

###  graphs ###
## U0 ##
fig0 = plt.figure(0)
plt.plot(Y,U0,"*")
plt.xlabel('Y [m]')
plt.ylabel('U0')
plt.title('U0 versus Y')	
plt.grid()
fig0.savefig("U0.png")
## U1 ##
fig1 = plt.figure(1)
plt.plot(Y,U1,"*")
plt.xlabel('Y [m]')
plt.ylabel('U1')
plt.title('U1 versus Y')	
plt.grid()
fig0.savefig("U1.png")
## U1 ##
fig2 = plt.figure(2)
plt.plot(Y,U2,"*")
plt.xlabel('Y [m]')
plt.ylabel('U2')
plt.title('U2 versus Y')	
plt.grid()
fig0.savefig("U2.png")
## U ##
fig3 = plt.figure(3)
plt.plot(Y,U0,"*",Y,U1,'-',Y,U2,'.')
plt.xlabel('Y [m]')
plt.ylabel('U')
plt.title('U versus Y')	
plt.legend(("U0","U1","U2"),loc='center left', bbox_to_anchor=(0.6,0.815), numpoints=2)
#plt.grid()
fig3.savefig("U.png")

