# 1.
import sys
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

x = np.array ([90, 85, 90, 95, 100, 110, 115, 120, 125])
y = np.array ([240, 250, 260, 270, 280, 290, 300, 310, 320])

plt.plot(x,y)

plt.xlabel ("Average Pulse")
plt.ylabel ("Calorie Burnage")

plt.show()


#2.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x = np.array ([0, 1, 2, 3])
y = np. array ([3, 8, 1, 10])

plt.subplot (1, 2, 1)
plt.plot(x,y)

plt.show()


#3. 
import sys
import matplotlib

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()


#4. 
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x= ["Apples", "Bananas"]
y = [400, 350]

plt.bar(x,y)
plt.show