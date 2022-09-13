# library & dataset
import matplotlib.pyplot as plt
import numpy as np

def parabel(x):
  return x**2

def populateArray(start, end) -> list[int]:
  returnArray = []
  for i in range(start, end+1):
    returnArray.append(i)
  return returnArray


x = np.array(populateArray(-5,5))

# Make default density plot
plt.plot(x, parabel(x), 'r')
plt.show()