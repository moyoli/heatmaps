import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import seaborn as sns
data = pd.read_csv("Heatmap_testdata.csv")
#create figure
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
fig.set_size_inches(7,5)
#pitch outline and centreline
plt.plot([0, 0], [0, 90], color="black")
plt.plot([0,130],[90,90], color="black")
plt.plot([130,130],[90,0], color="black")
plt.plot([130,0],[0,0], color="black")
plt.plot([65,65],[0,90], color="black")
#left side penalty area
plt.plot([16.5, 16.5],[65,25], color="black")
plt.plot([0,16.5],[65,65], color="black")
plt.plot([16.5,0],[25,25], color="black")
#right side penalty area
plt.plot([130, 113.5], [65, 65], color="black")
plt.plot([113.5, 113.5], [65, 25], color="black")
plt.plot([113.5, 130], [25, 25], color="black")
#left six-yard box
plt.plot([0, 5.5], [54, 54], color="black")
plt.plot([5.5, 5.5], [54, 36], color="black")
plt.plot([5.5, 0.5], [36, 36], color="black")
#right six-yard box
plt.plot([130, 124.5], [54, 54], color="black")
plt.plot([124.5, 124.5], [54, 36], color="black")
plt.plot([124.5, 130], [36, 36], color="black")
#assign circles to variables without filling circle
centreCircle = plt.Circle((65,45),9.15,COLOR="black",fill=False)
centreSpot = plt.Circle((65,45),0.8,color="black")
leftPenSpot = plt.Circle((11,45),0.8,color="black")
rightPenSpot = plt.Circle((119,45),0.8,color="black")
#draw the circles to the plot
ax.add_patch(centreCircle)
ax.add_patch(centreSpot)
ax.add_patch(leftPenSpot)
ax.add_patch(rightPenSpot)
#Arcs
leftArc = Arc((11,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="black")
rightArc = Arc((119,45),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="black")
#drawarcs
ax.add_patch(leftArc)
ax.add_patch(rightArc)
#Tidy axes
plt.axis('off')
sns.kdeplot(data["Xstart"],data["Ystart"],shade="True",n_levels=50)
plt.ylim(0, 90)
plt.xlim(0, 130)
#displaypitch
plt.show()