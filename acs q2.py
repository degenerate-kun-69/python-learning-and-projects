import matplotlib.pyplot as plt

# Given data
class_intervals = ['Below 375', '375-450', '450-525', '525-600', '600-675', '675-750', '750-825']
midpoints = [187.5, 412.5, 487.5, 562.5, 637.5, 712.5, 787.5]
frequencies = [69, 167, 207, 65, 58, 24, 110]

# Calculate cumulative frequencies
cumulative_frequencies = [sum(frequencies[:i+1]) for i in range(len(frequencies))]

# Plotting the ogive
plt.figure(figsize=(10, 5))
plt.plot(midpoints, cumulative_frequencies, marker='o', linestyle='-', color='b', label='Ogive')
plt.title('Ogive')
plt.xlabel('Midpoints')
plt.ylabel('Cumulative Frequencies')
plt.grid(True)
plt.legend()
plt.show()

# Plotting the frequency polygon
plt.figure(figsize=(10, 5))
plt.plot(midpoints, frequencies, marker='o', linestyle='-', color='g', label='Frequency Polygon')
plt.title('Frequency Polygon')
plt.xlabel('Midpoints')
plt.ylabel('Frequencies')
plt.grid(True)
plt.legend()
plt.show()

# Plotting the histogram
plt.figure(figsize=(10, 5))
plt.hist(midpoints, bins=8, weights=frequencies, edgecolor='black', color='orange', alpha=0.7, label='Histogram')
plt.title('Histogram')
plt.xlabel('Midpoints')
plt.ylabel('Frequencies')
plt.grid(True)
plt.legend()
plt.show()
