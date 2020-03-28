# importing the required module
import matplotlib.pyplot as plt
from statistics import mean, median
# frequencies
prices = [50, 60, 45, 30, 45, 70, 63, 52, 300, 350, 73, 72, 64, 64, 59, 53, 185, 253, 129, 152, 239, 278, 210]

# setting the range and no. of intervals
range = (40, 350)
bins = 10

# plotting a histogram
plt.hist(prices, bins, range, color = 'blue', histtype = 'bar', rwidth = 0.8)

# x-axis label
plt.xlabel('price in hundred thousnads')

# frequency label
plt.ylabel('No. of houses')

# plot title
plt.title('Right skewed histogram of # of houses vs price')

# plot interpretation
plt.text(
80, 
8, 
'''
The median = 700k is a more accurate indicator of how much a "typical" house would cost than the mean = 1.26m in this poll of data.
The wide range in prices of "expensive" houses shaped the histogram in a right skewed fashion.
Interestingly, one could make a statement that there are just as many "typical" houses and "expensive" houses for the given data because
there are 11 houses fall into the range of 430k to 680k, and also 11 houses fall outside of 430k to 680k.
While that might be a valid statement, one should pay attention to the wide range in prices of "expensive" houses that fall ourside of 430k to 680k.
These "expensive" houses have the prince range of 700k (median) all the way to 350m.
''', 
horizontalalignment='left')

# cal mean
print('mean:', mean(prices))

# cal median
print('median:', median(prices))

# function to show the plot
plt.show()
