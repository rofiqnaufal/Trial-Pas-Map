import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc



data = pd.read_csv(r"D:\Downloads\events (5).csv")
data['X'] = data['X']*1.3
data['Y'] = data['Y']*0.9
data['X2'] = data['X2']*1.3
data['Y2'] = data['Y2']*0.9

print(data)

# Create figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Pitch Outline & Centre Line
plt.plot([0, 0], [0, 90], color="black")
plt.plot([0, 130], [90, 90], color="black")
plt.plot([130, 130], [90, 0], color="black")
plt.plot([130, 0], [0, 0], color="black")
plt.plot([65, 65], [0, 90], color="black")

# Left Penalty Area
plt.plot([16.5, 16.5], [65, 25], color="black")
plt.plot([0, 16.5], [65, 65], color="black")
plt.plot([16.5, 0], [25, 25], color="black")

# Right Penalty Area
plt.plot([130, 113.5], [65, 65], color="black")
plt.plot([113.5, 113.5], [65, 25], color="black")
plt.plot([113.5, 130], [25, 25], color="black")

# Left 6-yard Box
plt.plot([0, 5.5], [54, 54], color="black")
plt.plot([5.5, 5.5], [54, 36], color="black")
plt.plot([5.5, 0.5], [36, 36], color="black")

# Right 6-yard Box
plt.plot([130, 124.5], [54, 54], color="black")
plt.plot([124.5, 124.5], [54, 36], color="black")
plt.plot([124.5, 130], [36, 36], color="black")

# Prepare Circles
centreCircle = plt.Circle((65, 45), 9.15, color="black", fill=False)
centreSpot = plt.Circle((65, 45), 0.8, color="black")
leftPenSpot = plt.Circle((11, 45), 0.8, color="black")
rightPenSpot = plt.Circle((119, 45), 0.8, color="black")

# Draw Circles
ax.add_patch(centreCircle)
ax.add_patch(centreSpot)
ax.add_patch(leftPenSpot)
ax.add_patch(rightPenSpot)

# Prepare Arcs
leftArc = Arc((11, 45), height=18.3, width=18.3, angle=0, theta1=310, theta2=50, color="black")
rightArc = Arc((119, 45), height=18.3, width=18.3, angle=0, theta1=130, theta2=230, color="black")

# Draw Arcs
ax.add_patch(leftArc)
ax.add_patch(rightArc)

# Tidy Axes
plt.axis('off')


# Plotting the passes
for i in range(len(data)):
   if data["Outcome"][i] == "Successful":
        plt.scatter(data["X"][i], data["Y"][i], color="black")
        x,y= (data["X"][i]), (data["Y"][i])
        dx,dy = (float(data["X2"][i]))-(float((data["X"][i]))), (float(data["Y2"][i]))-(float((data["Y"][i])))
        plt.arrow(x,y,dx,dy, width=0.2, head_width=2, color="green",linestyle="-", label="Successful")
   if data["Outcome"][i] == "Failed":
       plt.scatter(data["X"][i], data["Y"][i], color="black")
       x, y = (data["X"][i]), (data["Y"][i])
       dx, dy = (float(data["X2"][i])) - (float((data["X"][i]))), (float(data["Y2"][i])) - (float((data["Y"][i])))
       plt.arrow(x, y, dx, dy, width=0.2, head_width=2, color="red",linestyle=":", label="Unsuccessful")

#Legend
plt.legend(bbox_to_anchor=(0.2, 0.05))

plt.title("Trial pass map",color="black",size=20)


plt.show()
