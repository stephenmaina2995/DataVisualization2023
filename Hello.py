import csv
import numpy as np
from matplotlib import pyplot as plt

# dev_x = []

# dev_y= []

# plt.plot(dev_x, dev_y)

# plt.show()
plt.style.use("fivethirtyeight")
with open('Hello.csv') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    
    row = next(csv_reader)
    print (row['email'])