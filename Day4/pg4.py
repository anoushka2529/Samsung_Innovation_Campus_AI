import matplotlib.pyplot as plt
import numpy as np

labels = ['Math', 'Science', 'English', 'History']
sizes = [25, 30, 20, 25]
colors = ['gold', 'lightblue', 'lightgreen', 'pink']


angles = np.linspace(0, 2 * np.pi, len(sizes), endpoint=False)
sizes = np.array(sizes)
sizes = sizes / sizes.max()  

fig, ax = plt.subplots(subplot_kw={'polar': True})
bars = ax.bar(angles, sizes, width=0.5, color=colors, alpha=0.7)

ax.set_xticks(angles)
ax.set_xticklabels(labels)
ax.set_yticklabels([])
plt.title("Subject Distribution (Polar Area Plot)")
plt.show()