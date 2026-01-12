import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import numpy as np
from matplotlib.collections import PolyCollection  
from matplotlib.colors import Normalize 



    # phisical activity + sleep  VS mental health condition
data_set = pd.read_csv('data.csv', header = 0, usecols= ['Physical_Activity', 'Sleep_Quality', 'Mental_Health_Condition'], na_filter=False)
    # find cols
x_phy = data_set['Physical_Activity']
y_sle = data_set['Sleep_Quality']
z_men = data_set['Mental_Health_Condition']

    # map the status as nums
physical_mapping = {
        'None': 2,
        'Weekly': 1,
        'Daily': 0
}
sleep_mapping = {
    'Poor': 2,
    'Average': 1,
    'Good': 0
}
mental_mapping = {
    'None': 0,
    'Anxiety': 1,
    'Burnout': 2,
    'Depression': 3
}
    # replace them
x = [physical_mapping[status] for status in x_phy]
y = [sleep_mapping[status] for status in y_sle]
z = [mental_mapping[status] for status in z_men]


    # calculate density and normalize
num_points = 5000
density = np.zeros((4, 4, 4), dtype=int) 
for i in range(num_points):  
    density[x[i], y[i], z[i]] += 1  
density_normalized = density / density.max() 
    # create a graphic object
fig = plt.figure()
    # create a 3D coordinate axis
ax = fig.add_subplot(111, projection='3d')
    # use color
# color = sns.color_palette("Purples", as_cmap=False)
# scatter_color = color[5]
colors = []  
for i in range(num_points):  
    colors.append(density_normalized[x[i], y[i], z[i]])  
    
colors = np.array(colors) 
norm = plt.Normalize(vmin=0, vmax=1) 
sc = ax.scatter(x, y, z, c=colors, cmap='viridis', norm=norm, edgecolor='none', s=50)  


cbar = fig.colorbar(sc, ax=ax, label='density')


#ax.scatter(re_x_phy, re_y_sle, re_z_men, c=scatter_color, marker='o')
ax.set_xlabel('Physical_Activity')
ax.set_ylabel('Sleep_Quality')
ax.set_zlabel('Mental_Health_Condition')
ax.set_title('Physical activity and sleep versus mental health condition')
plt.show()
# fig.write_html('show2.html')
    






