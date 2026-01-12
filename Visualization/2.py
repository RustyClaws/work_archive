import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import numpy as np
from matplotlib.collections import PolyCollection  
from matplotlib.colors import Normalize 

    # work location + visual meetings VS social isolation
data_set = pd.read_csv('data.csv', header = 0, na_filter=False, usecols= ['Work_Location', 'Number_of_Virtual_Meetings', 'Social_Isolation_Rating'])
    # map the status as nums
location_mapping = {
    'Onsite': 0,
    'Hybrid': 1,
    'Remote': 2
}
x_location = data_set['Work_Location']
y = data_set['Number_of_Virtual_Meetings']
z = data_set['Social_Isolation_Rating']

    # replace locations as nums
x= [location_mapping[status] for status in x_location]


num_points = 5000
density = np.zeros((4, 16, 6), dtype=int) 
for i in range(num_points):  
    density[x[i], y[i], z[i]] += 1  
density_normalized = density / density.max() 

    # create a graphic object
fig = plt.figure()
    # create a 3D coordinate axis
ax = fig.add_subplot(111, projection='3d')
    # use color


colors = []  
for i in range(num_points):  
    colors.append(density_normalized[x[i], y[i], z[i]])  
colors = np.array(colors) 
norm = plt.Normalize(vmin=0, vmax=1) 
sc = ax.scatter(x, y, z, c=colors, cmap='viridis', norm=norm, edgecolor='none', s=50)  


cbar = fig.colorbar(sc, ax=ax, label='密度')
# color = sns.color_palette("Purples", as_cmap=False)
# scatter_color = color[4]
# ax.scatter(re_x_location, y_vir, z_social, c=scatter_color, marker='o')
ax.set_xlabel('Work_Location')
ax.set_ylabel('Number_of_Virtual_Meetings')
ax.set_zlabel('Social_Isolation_Rating')
ax.set_title('Work location and virtual meetings versus social isolation')
plt.show()