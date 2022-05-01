# -*- coding: utf-8 -*-
"""perf_plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tefQzzXe346phudmokzci5e0TX3E2jF_
"""

# importing package
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = (20,3) 
  
# create data
x1 = [1.37,1.27,1.19,1.32,1.49]
x2 = [1.46,1.24,1.27,1.23,1.52]
y = [30,60,90,120,150]
  
# plot lines
plt.plot (y,x1, label = "DDQN", linestyle="-",linewidth=2,marker = 'o',c = 'b')
plt.plot (y,x2, label = "DQN", linestyle=":",linewidth=2,marker = '*',c = 'r')
plt.xticks(np.arange(min(y), max(y)+30, 30))
plt.ylabel("Power Consumption ( in Watt. (W) )")
plt.xlabel("Time (in sec)")
plt.title("Power Consumption Analysis", fontsize = 15)
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1.75
plt.legend()
plt.show()

# importing package
import matplotlib.pyplot as plt
import numpy as np
  
# create data
x1 = [1249.557373,2192.521423,3258.163452,4267.169800,5572.356201]
x2 = [1166.214600,2403.948608,3307.811096,4071.044434,5280.595581]
y = [30,60,90,120,150]
  
# plot lines
plt.plot (y,x1, label = "DQN", linestyle="-",linewidth=2,marker = 'o',c = 'm')
plt.plot (y,x2, label = "DDQN", linestyle="--",linewidth=2,marker = 'X',c = 'g')
plt.xticks(np.arange(min(y), max(y)+30, 30))
plt.ylabel("Energy Dissipated ( in Joules (J) )")
plt.xlabel("Time (in sec)")
plt.title("Energy dissipation (CPU Socket)", fontsize = 15)
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1.75
plt.legend()
plt.show()

# importing package
import matplotlib.pyplot as plt
import numpy as np
  
# create data
x1 = [947.264221,1668.632141,2495.140076,3249.232849,4292.753479]
x2 = [885.429138,1874.832947,1874.832947,3104.026672,4029.201477]
y = [30,60,90,120,150]
  
# plot lines
plt.plot (y,x1, label = "DQN", linestyle="-",linewidth=2,marker = 'o',c = 'r')
plt.plot (y,x2, label = "DDQN", linestyle="--",linewidth=2,marker = 'X',c = '#ffbb11')
plt.xticks(np.arange(min(y), max(y)+30, 30))
plt.ylabel("Energy Dissipated ( in Joules (J) )")
plt.xlabel("Time (in sec)")
plt.title("Energy dissipation (All CPU Cores)", fontsize = 15)
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1.75
plt.legend()
plt.show()

# importing package
import matplotlib.pyplot as plt
import numpy as np
  
# create data
x1 = [2.094482,3.657471,4.501221,4.852661,6.805908]
x2 = [2.517944,4.004089,4.501221,4.852661,6.805908]
y = [30,60,90,120,150]
  
# plot lines
plt.plot (y,x1, label = "DDQN", linestyle="-",linewidth=2,marker = 'o',c = 'c')
plt.plot (y,x2, label = "DQN", linestyle="--",linewidth=2,marker = 'X',c = 'y')
plt.xticks(np.arange(min(y), max(y)+30, 30))
plt.ylabel("Energy Dissipated ( in Joules (J) )")
plt.xlabel("Time (in sec)")
plt.title("Energy dissipation (Uncore Components)", fontsize = 15)
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1.75
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#plt.rcParams["figure.figsize"] = (28,6)  

N = 8
ind = np.arange(N) 
width = 0.35

x1 = [41,40,35,40,35,51,37,39]
bar1 = plt.bar(ind, x1, width=0.2, color = 'b')
  
x2 = [47,48,45,61,45,48,46,47]
bar2 = plt.bar(ind+width, x2, width=0.2, color='g')

plt.ylabel("Temperature (in o'C)", fontsize = 15)
plt.xlabel("Different Cores (Intel Processor)", fontsize = 15)
plt.title("Effect on Temperature  on different cores", fontsize = 15)
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1.75

plt.xticks(ind+width,['Core 0','Core 1','Core 2','Core 3','Core 4','Core 5','Core 6','Core 7'])
plt.tick_params(rotation=25)
plt.legend( (bar1, bar2), ('DDQN', 'DQN') )
plt.show()