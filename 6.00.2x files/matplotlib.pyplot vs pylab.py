# Matplotlib is the whole package; pylab is a module in matplotlib that gets installed alongside matplotlib; 
# and matplotlib.pyplot is a module in matplotlib. Pyplot provides the state-machine interface to the underlying
# plotting library in matplotlib. This means that figures and axes are implicitly and automatically created to 
# achieve the desired plot. For example, calling plot from pyplot will automatically create the necessary figure 
# and axes to achieve the desired plot. Setting a title will then automatically set that title to the current 
# axes object:

# Pylab combines the pyplot functionality (for plotting) with the numpy functionality (for mathematics and for 
# working with arrays) in a single namespace, making that namespace (or environment) even more MATLAB-like. 
# For example, one can call the sin and cos functions just like you could in MATLAB, as well as having all the 
# features of pyplot.

# The pyplot interface is generally preferred for non-interactive plotting (i.e., scripting). 
# The pylab interface is convenient for interactive calculations and plotting, as it minimizes 
# typing. Note that this is what you get if you use the ipython shell with the -pylab option, 
# which imports everything from pylab and makes plotting fully interactive.

import matplotlib.pyplot as plt


plt.plot([1,2,3],[4,5,6])
